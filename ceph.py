from __main__ import vtk, qt, ctk, slicer
import numpy
from vtk.util import numpy_support
import SimpleITK as sitk
global im;
#
# HelloPython
#

class ceph:
  def __init__(self, parent):
    parent.title = "Cephalomety"
    parent.categories = ["Maxillofacial"]
    parent.dependencies = []
    parent.contributors = ["Jose de Jesus Montufar Trujillo, MSc, Facultad de Ingenieria, UAEMex\nMarcelo Romero Huertas, PhD, Facultad de Ingenieria, UAEMex"]
    parent.helpText = "Module from a python script for automatic cephalometric analysis."
    parent.acknowledgementText = "Facultad de Ingenieria, Facultad de Odontologia, UAEMex, CONACYT" # replace with organization, grant and thanks.
    self.parent = parent

#
# qHelloPythonWidget
#

class cephWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # Collapsible button
    cButton = ctk.ctkCollapsibleButton()
    cButton.text = "GENERAL"
    self.layout.addWidget(cButton)

    dButton = ctk.ctkCollapsibleButton()
    dButton.text = "SIMULAR X-RAYS"
    self.layout.addWidget(dButton)
    
    eButton = ctk.ctkCollapsibleButton()
    eButton.text = "ANALISIS CEFALOMETRICO"
    self.layout.addWidget(eButton)

    # Layout within the sample collapsible button
    sampleFormLayout = qt.QFormLayout(cButton)

    hButton = qt.QPushButton('CARGAR DICOM')
    hButton.toolTip = "CARGAR IMAGENES DICOM"
    sampleFormLayout.addWidget(hButton)
    hButton.connect('clicked(bool)', self.onHButtonClicked)
    
    b=qt.QPushButton('INFO')
    b.toolTip = "Informacion acerca del volumen que sera renderizado"
    sampleFormLayout.addWidget(b)
    b.connect('clicked(bool)',self.boton)
    
    hec=qt.QPushButton('REINICIAR MODULO')
    hec.toolTip = "Volver a cargar este modulo"
    sampleFormLayout.addWidget(hec)
    hec.connect('clicked()',self.hec)
    
    # Layout within the sample collapsible button
    sampleFormLayout = qt.QFormLayout(dButton)
    
    mip=qt.QPushButton('MIP PROJECTION')
    mip.toolTip = "Algoritmo de proyeccion MIP"
    sampleFormLayout.addWidget(mip)
    mip.connect('clicked(bool)',self.mip)
    
    rsum=qt.QPushButton('RAY-SUM PROJECTION')
    rsum.toolTip = "Algoritmo de proyeccion Ray Sum"
    sampleFormLayout.addWidget(rsum)
    rsum.connect('clicked(bool)',self.rsum)

    # Add vertical spacer
    self.layout.addStretch(1)

    # Set local var as instance attribute
    self.hButton = hButton
    self.b = b
    self.hec = hec
    self.mip=mip

  def onHButtonClicked(self):
    i = ctk.ctkDICOMIndexer()
    i.addDirectory(slicer.dicomDatabase, '/Users/Research/Documents/DICOM Files/TAC MONSERRAT')
    m = slicer.util.mainWindow()
    m.moduleSelector().selectModule('DICOM')

    
  def boton(self):
    n = slicer.util.getNode('2: Unknown')
    print(n);
    print('INFO DE VOLUMEN');
  

  def hec(self):
    print "REINICIANDO..."
    slicer.util.reloadScriptedModule('ceph')
    qt.QMessageBox.information(slicer.util.mainWindow(),'Slicer','Listo!')
    print "Listo\n"
  
  def rsum(self):
    qt.QMessageBox.information(slicer.util.mainWindow(),'Slicer','Working on it!')
    print "Next\n"
      
  def mip(self):
    a = slicer.util.array('2: Unknown')
    im = numpy.zeros(shape=(a.shape[1],a.shape[2]))
    im.dtype='int16'
    for i in range (1,a.shape[1]):
        for j in range (1,a.shape[2]):
            im[i,j]=max(a[:,i,j])
    print im
    a=a.astype(float);
    ############################################################
    
    image = sitk.Image(512, 512, 1, sitk.sitkInt16)
    img = sitk.GetImageFromArray(im)
    print img.GetSize()
    sitk.Show(img)
    img.GetSize()
    img
    inputImage = sitkUtils.PullFromSlicer('im')
    filter = sitk.SignedMaurerDistanceMapImageFilter()
    outputImage = filter.Execute(inputImage)
    sitkUtils.PushToSlicer(img,'outputImage')
    
    
    lll

    ############################################################
    
    
    
    print "DONE"



#def botong():
#  print('HI!')
#b=qt.QPushButton('Boton de Prueba')
#b.connect('clicked()',botong)
#b.show()


