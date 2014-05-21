from pycegid.export import ExportTra
from pycegid.tools import position


class TestExportVersion009(object):

    def test_header(self):
        tra = ExportTra()
        tra.changeFormat('009')
        tra.setHeader('S5', 'CLI', 'JRL', num_dossier='B105ZZ')
        content = tra.render()
        assert position(content, 34, 3) == '009'
