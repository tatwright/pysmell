import unittest
from pysmell.vimhelper import findWord, findBase

class MockVim(object):
    class _current(object):
        class _window(object):
            cursor = (-1, -1)
        buffer = []
        window = _window()
    current = _current()
    command = lambda _, __:Non
    def eval(*_):
        pass

class VimHelperTest(unittest.TestCase):

    def setUp(self):
        import pysmell.vimhelper
        pysmell.vimhelper.vim = self.vim = MockVim()

    def testFindBaseName(self):
        self.vim.current.buffer = ['aaaa', 'bbbb', 'cccc']
        self.vim.current.window.cursor =(2, 2)
        index = findBase('bbbb', 2)
        word = findWord(self.vim, 2, 'bbbb')
        self.assertEquals(index, 0)
        self.assertEquals(word, 'bb')

    def testFindBaseMethodCall(self):
        self.vim.current.buffer = ['aaaa', 'a.bbbb(', 'cccc']
        self.vim.current.window.cursor =(2, 7)
        index = findBase('a.bbbb(', 7)
        word = findWord(self.vim, 7, 'a.bbbb(')
        self.assertEquals(index, 2)
        self.assertEquals(word, 'a.bbbb(')

    def testFindBaseFuncCall(self):
        self.vim.current.buffer = ['aaaa', 'bbbb(', 'cccc']
        self.vim.current.window.cursor =(2, 5)
        index = findBase('bbbb(', 5)
        word = findWord(self.vim, 5, 'bbbb(')
        self.assertEquals(index, 0)
        self.assertEquals(word, 'bbbb(')

    def testFindBaseNameIndent(self):
        self.vim.current.buffer = ['aaaa', '    bbbb', 'cccc']
        self.vim.current.window.cursor =(2, 6)
        index = findBase('    bbbb', 6)
        word = findWord(self.vim, 6, '    bbbb')
        self.assertEquals(index, 4)
        self.assertEquals(word, 'bb')

    def testFindBaseProp(self):
        self.vim.current.buffer = ['aaaa', 'hehe.bbbb', 'cccc']
        self.vim.current.window.cursor =(2, 7)
        index = findBase('hehe.bbbb', 7)
        word = findWord(self.vim, 7, 'hehe.bbbb')
        self.assertEquals(index, 5)
        self.assertEquals(word, 'hehe.bb')

    def testFindBasePropIndent(self):
        self.vim.current.buffer = ['aaaa', '    hehe.bbbb', 'cccc']
        self.vim.current.window.cursor =(2, 11)
        index = findBase('    hehe.bbbb', 11)
        word = findWord(self.vim, 11, '    hehe.bbbb')
        self.assertEquals(index, 9)
        self.assertEquals(word, 'hehe.bb')

if __name__ == '__main__':
    unittest.main()
