# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Gestão de Perfumes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuMarcas = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Marcas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuMarcas )

		self.menuEssencias = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Essências", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuEssencias )

		self.menuFixacoes = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Fixações", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuFixacoes )

		self.menuVolume = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Volume", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuVolume )

		self.m_menubar1.Append( self.m_menu1, u"Cadrastros Básicos" )

		self.m_menu2 = wx.Menu()
		self.menuPerfumes = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Perfumes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumes )

		self.menuPerfumeEssencia() = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Essência do Perfume", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumeEssencia() )

		self.m_menubar1.Append( self.m_menu2, u"Perfumes" )

		self.m_menu3 = wx.Menu()
		self.menuSobre = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sobre", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSobre )

		self.menuSair = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sair", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSair )

		self.m_menubar1.Append( self.m_menu3, u"Ajuda" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.abrirMarcas(), id = self.menuMarcas.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirEssencias(), id = self.menuEssencias.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirFixacoes(), id = self.menuFixacoes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirVolume, id = self.menuVolume.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfumes(), id = self.menuPerfumes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfumeEssencia(), id = self.menuPerfumeEssencia().GetId() )
		self.Bind( wx.EVT_MENU, self.abrirSobre(), id = self.menuSobre.GetId() )
		self.Bind( wx.EVT_MENU, self.sair(), id = self.menuSair.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def abrirMarcas()( self, event ):
		event.Skip()

	def abrirEssencias()( self, event ):
		event.Skip()

	def abrirFixacoes()( self, event ):
		event.Skip()

	def abrirVolume( self, event ):
		event.Skip()

	def abrirPerfumes()( self, event ):
		event.Skip()

	def abrirPerfumeEssencia()( self, event ):
		event.Skip()

	def abrirSobre()( self, event ):
		event.Skip()

	def sair()( self, event ):
		event.Skip()


###########################################################################
## Class FrameMarca
###########################################################################

class FrameMarca ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marcas", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Descrição: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 0 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.gridMarcas = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridMarcas.CreateGrid( 0, 2 )
		self.gridMarcas.EnableEditing( True )
		self.gridMarcas.EnableGridLines( True )
		self.gridMarcas.EnableDragGridSize( False )
		self.gridMarcas.SetMargins( 0, 0 )

		# Columns
		self.gridMarcas.SetColSize( 0, 30 )
		self.gridMarcas.SetColSize( 1, 300 )
		self.gridMarcas.EnableDragColMove( False )
		self.gridMarcas.EnableDragColSize( True )
		self.gridMarcas.SetColLabelSize( 30 )
		self.gridMarcas.SetColLabelValue( 0, u"ID" )
		self.gridMarcas.SetColLabelValue( 1, u"Nome" )
		self.gridMarcas.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridMarcas.EnableDragRowSize( True )
		self.gridMarcas.SetRowLabelSize( 80 )
		self.gridMarcas.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridMarcas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.gridMarcas, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame() )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarMarca() )
		self.gridMarcas.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame()( self, event ):
		event.Skip()

	def adicionarMarca()( self, event ):
		event.Skip()

	def atualizarMarca()( self, event ):
		event.Skip()


###########################################################################
## Class FrameEssencias
###########################################################################

class FrameEssencias ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Essências", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adcionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.gridEssencias = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridEssencias.CreateGrid( 0, 2 )
		self.gridEssencias.EnableEditing( False )
		self.gridEssencias.EnableGridLines( True )
		self.gridEssencias.EnableDragGridSize( False )
		self.gridEssencias.SetMargins( 0, 0 )

		# Columns
		self.gridEssencias.SetColSize( 0, 30 )
		self.gridEssencias.SetColSize( 1, 300 )
		self.gridEssencias.EnableDragColMove( False )
		self.gridEssencias.EnableDragColSize( True )
		self.gridEssencias.SetColLabelSize( 30 )
		self.gridEssencias.SetColLabelValue( 0, u"ID" )
		self.gridEssencias.SetColLabelValue( 1, u"Nome" )
		self.gridEssencias.SetColLabelValue( 2, u"ID" )
		self.gridEssencias.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridEssencias.EnableDragRowSize( True )
		self.gridEssencias.SetRowLabelSize( 80 )
		self.gridEssencias.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridEssencias.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.gridEssencias, 1, wx.ALL, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame() )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarEssencia() )
		self.gridEssencias.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarEssencia() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame()( self, event ):
		event.Skip()

	def adicionarEssencia()( self, event ):
		event.Skip()

	def atualizarEssencia()( self, event ):
		event.Skip()


###########################################################################
## Class FrameFixacoes
###########################################################################

class FrameFixacoes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fixações", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.gridFixacoes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridFixacoes.CreateGrid( 0, 2 )
		self.gridFixacoes.EnableEditing( True )
		self.gridFixacoes.EnableGridLines( True )
		self.gridFixacoes.EnableDragGridSize( False )
		self.gridFixacoes.SetMargins( 0, 0 )

		# Columns
		self.gridFixacoes.SetColSize( 0, 30 )
		self.gridFixacoes.SetColSize( 1, 300 )
		self.gridFixacoes.EnableDragColMove( False )
		self.gridFixacoes.EnableDragColSize( True )
		self.gridFixacoes.SetColLabelSize( 30 )
		self.gridFixacoes.SetColLabelValue( 0, u"ID" )
		self.gridFixacoes.SetColLabelValue( 1, u"Nome" )
		self.gridFixacoes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridFixacoes.EnableDragRowSize( True )
		self.gridFixacoes.SetRowLabelSize( 80 )
		self.gridFixacoes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridFixacoes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.gridFixacoes, 1, wx.ALL, 5 )


		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame() )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarFixacoes )
		self.gridFixacoes.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarFixacoes() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame()( self, event ):
		event.Skip()

	def adicionarFixacoes( self, event ):
		event.Skip()

	def atualizarFixacoes()( self, event ):
		event.Skip()


###########################################################################
## Class FrameVolume
###########################################################################

class FrameVolume ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Volume", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4.CreateGrid( 0, 2 )
		self.m_grid4.EnableEditing( True )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )

		# Columns
		self.m_grid4.SetColSize( 0, 30 )
		self.m_grid4.SetColSize( 1, 300 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelValue( 0, u"ID" )
		self.m_grid4.SetColLabelValue( 1, u"Nome" )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4.EnableDragRowSize( True )
		self.m_grid4.SetRowLabelSize( 80 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.m_grid4, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame() )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarVolume() )
		self.m_grid4.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarVolume() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame()( self, event ):
		event.Skip()

	def adicionarVolume()( self, event ):
		event.Skip()

	def atualizarVolume()( self, event ):
		event.Skip()


###########################################################################
## Class FramePerfumes
###########################################################################

class FramePerfumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Perfumes", pos = wx.DefaultPosition, size = wx.Size( 517,292 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.gridPerfumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridPerfumes.CreateGrid( 0, 6 )
		self.gridPerfumes.EnableEditing( True )
		self.gridPerfumes.EnableGridLines( True )
		self.gridPerfumes.EnableDragGridSize( False )
		self.gridPerfumes.SetMargins( 0, 0 )

		# Columns
		self.gridPerfumes.SetColSize( 0, 30 )
		self.gridPerfumes.SetColSize( 1, 200 )
		self.gridPerfumes.SetColSize( 2, 100 )
		self.gridPerfumes.SetColSize( 3, 200 )
		self.gridPerfumes.SetColSize( 4, 200 )
		self.gridPerfumes.SetColSize( 5, 200 )
		self.gridPerfumes.EnableDragColMove( False )
		self.gridPerfumes.EnableDragColSize( True )
		self.gridPerfumes.SetColLabelSize( 30 )
		self.gridPerfumes.SetColLabelValue( 0, u"ID" )
		self.gridPerfumes.SetColLabelValue( 1, u"Nome" )
		self.gridPerfumes.SetColLabelValue( 2, u"Quantidade" )
		self.gridPerfumes.SetColLabelValue( 3, u"Volume" )
		self.gridPerfumes.SetColLabelValue( 4, u"Marca" )
		self.gridPerfumes.SetColLabelValue( 5, wx.EmptyString )
		self.gridPerfumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridPerfumes.EnableDragRowSize( True )
		self.gridPerfumes.SetRowLabelSize( 80 )
		self.gridPerfumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridPerfumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer14.Add( self.gridPerfumes, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnAdicionar, 1, wx.ALL, 5 )

		self.btnSalvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnSalvar, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarPerfumes() )
		self.btnSalvar.Bind( wx.EVT_BUTTON, self.salvarPerfumes() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarPerfumes()( self, event ):
		event.Skip()

	def salvarPerfumes()( self, event ):
		event.Skip()


