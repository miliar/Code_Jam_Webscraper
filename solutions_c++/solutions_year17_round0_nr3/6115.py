
// CodeJam_WordSortDlg.cpp : ���� ����
//

#include "stdafx.h"
#include "CodeJam_WordSort.h"
#include "CodeJam_WordSortDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// ���� ���α׷� ������ ���Ǵ� CAboutDlg ��ȭ �����Դϴ�.

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// ��ȭ ���� �������Դϴ�.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV �����Դϴ�.

// �����Դϴ�.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CCodeJam_WordSortDlg ��ȭ ����



CCodeJam_WordSortDlg::CCodeJam_WordSortDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(IDD_CODEJAM_WORDSORT_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CCodeJam_WordSortDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CCodeJam_WordSortDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(ID_WORD_SORT, &CCodeJam_WordSortDlg::OnBnClickedWordSort)
	ON_BN_CLICKED(ID_MATRIX, &CCodeJam_WordSortDlg::OnBnClickedMatrix)
	ON_BN_CLICKED(IDC_OVERSIZED_PANCAKE, &CCodeJam_WordSortDlg::OnBnClickedOversizedPancake)
	ON_BN_CLICKED(IDC_Tidy_Numbers, &CCodeJam_WordSortDlg::OnBnClickedTidyNumbers)
	ON_BN_CLICKED(IDC_Bathroom_Stalls, &CCodeJam_WordSortDlg::OnBnClickedBathroomStalls)
END_MESSAGE_MAP()


// CCodeJam_WordSortDlg �޽��� ó����

BOOL CCodeJam_WordSortDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// �ý��� �޴��� "����..." �޴� �׸��� �߰��մϴ�.

	// IDM_ABOUTBOX�� �ý��� ��� ������ �־�� �մϴ�.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// �� ��ȭ ������ �������� �����մϴ�.  ���� ���α׷��� �� â�� ��ȭ ���ڰ� �ƴ� ��쿡��
	//  �����ӿ�ũ�� �� �۾��� �ڵ����� �����մϴ�.
	SetIcon(m_hIcon, TRUE);			// ū �������� �����մϴ�.
	SetIcon(m_hIcon, FALSE);		// ���� �������� �����մϴ�.

	// TODO: ���⿡ �߰� �ʱ�ȭ �۾��� �߰��մϴ�.

	return TRUE;  // ��Ŀ���� ��Ʈ�ѿ� �������� ������ TRUE�� ��ȯ�մϴ�.
}

void CCodeJam_WordSortDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// ��ȭ ���ڿ� �ּ�ȭ ���߸� �߰��� ��� �������� �׸�����
//  �Ʒ� �ڵ尡 �ʿ��մϴ�.  ����/�� ���� ����ϴ� MFC ���� ���α׷��� ��쿡��
//  �����ӿ�ũ���� �� �۾��� �ڵ����� �����մϴ�.

void CCodeJam_WordSortDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // �׸��⸦ ���� ����̽� ���ؽ�Ʈ�Դϴ�.

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Ŭ���̾�Ʈ �簢������ �������� ����� ����ϴ�.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// �������� �׸��ϴ�.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// ����ڰ� �ּ�ȭ�� â�� ���� ���ȿ� Ŀ���� ǥ�õǵ��� �ý��ۿ���
//  �� �Լ��� ȣ���մϴ�.
HCURSOR CCodeJam_WordSortDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}
CString SortString(CString strData)
{
	CString strSorted;
	strSorted = strData.Left(1);
	for (int iter = 1; iter < strData.GetLength(); iter++)
	{
		CString strCurrent = strData.Mid(iter, 1);
		if (strSorted.Left(1) > strCurrent)
		{
			strSorted.Append(strCurrent);
		}
		else
		{
			strSorted = strCurrent + strSorted;
		}
	}
	return strSorted;
}
CString ReadString(BYTE*& p)
{
	CString strValue;
	while (1)
	{
		if (*p == ' ' || *p == '\n' || *p == '\r')
		{
			p++;
			return strValue;
		}
		strValue.AppendChar(*p);
		p++;
	}
	return strValue;
}
LONGLONG ReadCountLongLong(BYTE*& p)
{
	LONGLONG ll;
	CString strValue = ReadString(p);
	return _tstoi64(strValue);

}
int ReadCount(BYTE*& p)
{	
	CString strValue = ReadString(p);
	return _ttoi(strValue);
}
void CCodeJam_WordSortDlg::OnBnClickedWordSort()
{
	CFileDialog dlg(TRUE);
	if (dlg.DoModal() == IDOK)
	{
		CFile f;
		if (f.Open(dlg.GetPathName(), CFile::modeRead))
		{
			int nLength = (int)f.GetLength();
			BYTE *pData = new BYTE[nLength];
			f.Read(pData, nLength);
			int nCount = ReadCount(pData);
			CFile fAnswer;
			fAnswer.Open(_T("d:\\Result.txt"), CFile::modeCreate | CFile::modeWrite);

			for (int iter = 0; iter < nCount; iter++)
			{
				char chResult[2000];
				CString str;
				str.Format(_T("Case #%d: "), iter + 1);
				CString strData = ReadString(pData);
				str.Append(SortString(strData));
				str.Append(_T("\r\n"));
				strcpy_s(chResult, 2000, CT2A(str));
				int nAnswer = strlen(chResult);
				fAnswer.Write(chResult, nAnswer);
			}
			fAnswer.Close();
			f.Close();

		}
	}
}

typedef struct _DATA
{
	int*pData;
	int nCount;
	int Number;
	BOOL bCol;
	_DATA(int nCnt)
	{
		nCount = nCnt;
		pData = new int[nCount];
		memset(pData, 0, sizeof(int)*nCount);
		Number = -1;
		bCol = FALSE;
	}
	~_DATA()
	{
		delete[] pData;
	}
};
void CCodeJam_WordSortDlg::OnBnClickedMatrix()
{
	CFileFind finder;
	
	
	BOOL bWorking = finder.FindFile(_T("d:\\20173*.jpg"));

	while (bWorking)
	{
		bWorking = finder.FindNextFile();
		if (finder.IsDots())
			continue;

		
		if (!finder.IsDirectory())
		{
			//���⼭ ó��	
		}
	}

		
	CFileDialog dlg(TRUE);
	if (dlg.DoModal() == IDOK)
	{
		CFile f;
		if (f.Open(dlg.GetPathName(), CFile::modeRead))
		{
			int nLength = (int)f.GetLength();
			BYTE *pData = new BYTE[nLength];
			f.Read(pData, nLength);
			int nCount = ReadCount(pData);
			CFile fAnswer;
			fAnswer.Open(_T("d:\\ResultB.txt"), CFile::modeCreate | CFile::modeWrite);
			fAnswer.SeekToBegin();

			for (int iter = 0; iter < nCount; iter++)
			{
				int N =  ReadCount(pData);
				int** pMatrix;
				pMatrix = new int*[N];
				
				for (int r = 0; r < N; r++)
				{
					pMatrix[r] = new int[N];
					memset(pMatrix[r], 0, sizeof(int)*N);
				}
				_DATA ** pData = new _DATA*[N*2];
				for (int i = 0; i < N * 2 - 1; i++)
				{
					//for (int x = 0; x < N);
				}
			}
			fAnswer.Close();
			f.Close();

		}
	}
}
void FlipData(BOOL* p, int nCount)
{
	for (int iter = 0; iter < nCount; iter++)
	{
		p[iter] = !p[iter];
	}
}
CString TraceCake(BOOL * p, int nCount)
{
	CString strResult;
	for (int iter = 0; iter < nCount; iter++)
	{
		if (p[iter])
		{
			strResult.Append(_T("+"));
		}
		else
		{
			strResult.Append(_T("-"));
		}
		
	}
	strResult.Append(_T("\r\n"));
	return strResult;
}
int SolveProblem1(BOOL* pData,int nDataCount, int nPanSize)
{
	int FlipCount = 0;
	int ConinueCount = 0;
	CString strResult = TraceCake(pData, nDataCount);
	for (int iter = 0; iter < nDataCount- nPanSize+1; iter++)
	{
		if (pData[iter] != TRUE)
		{
			FlipData(&pData[iter], nPanSize);
			strResult += TraceCake(pData, nDataCount);
			FlipCount++;
		}
	}

	BOOL bResult = TRUE;
	for (int iter = 0; iter < nPanSize; iter++)
	{
		if (pData[iter + nDataCount - nPanSize] != TRUE)
		{
			return -1;
		}
	}
	return FlipCount;

}
int SolveProblem1(BYTE* &pData)
{
	
	BOOL b[1000];
	int nCount = 0;
	int nPanSize = 0;
	for(int iter = 0 ; iter < 1000 ; iter ++)
	{
		nCount++;
		b[iter] = ((*pData) == '+');
		pData++;
		if (*pData == ' ' || *pData == '\n' || *pData == '\r')
		{
			pData++;
			nPanSize = ReadCount(pData);
			return SolveProblem1(b, nCount, nPanSize);
		}
	}


}
void CCodeJam_WordSortDlg::OnBnClickedOversizedPancake()
{
	CFileDialog dlg(TRUE);
	if (dlg.DoModal() == IDOK)
	{
		CFile f;
		if (f.Open(dlg.GetPathName(), CFile::modeRead))
		{
			int nLength = (int)f.GetLength();
			BYTE *pData = new BYTE[nLength];
			f.Read(pData, nLength);
			int nCount = ReadCount(pData);
			CFile fW;
			if (fW.Open(dlg.GetPathName() + _T(".out"), CFile::modeCreate | CFile::modeWrite))
			{
				for (int iter = 0; iter < nCount; iter++)
				{
					int nResult = SolveProblem1(pData);
					CString str;
					str.Format(_T("Case #%d: "), iter+1);
					if (nResult == -1)
					{
						str.Append(_T("IMPOSSIBLE\r\n"));
					}
					else
					{
						str.AppendFormat(_T("%d\r\n"), nResult);

					}
					char chResult[2000];
					strcpy_s(chResult, 2000, CT2A(str));
					int nAnswer = strlen(chResult);
					fW.Write(chResult, nAnswer);
				}
			}
			
		}
	}
}
CString SolveProblem2(CString strData)
{
	CString strResult;
	int nReplaceIndex = -1;
	for (int iter = 1; iter < strData.GetLength(); iter++)
	{
		if (strData.Mid(iter - 1, 1) > strData.Mid(iter , 1))
		{
			nReplaceIndex = iter-1;
			break;
		}
	}
	if (nReplaceIndex == -1)
	{
		return strData;

	}
	int nReplaceIndex2 = nReplaceIndex;
	for (int iter = nReplaceIndex; iter >0; iter--)
	{	
		if (strData.Mid(iter - 1, 1) == strData.Mid(iter, 1))
		{
			nReplaceIndex2 = iter - 1;
		}
	}
//	if (nReplaceIndex2 > 0)
	{
		strResult = strData.Left(nReplaceIndex2);
		strResult.AppendFormat(_T("%d"),_ttoi(strData.Mid(nReplaceIndex2,1))-1 );
	}
	for (int iter = nReplaceIndex2+1; iter < strData.GetLength(); iter++)
	{
		strResult.Append(_T("9"));
	}
	
	strResult.Replace(_T("0"), _T(""));

	return strResult;
}
CString SolveProblem2(BYTE* &pData)
{
	CString strResult;
	CString str;

	while (1)
	{
		if (*pData == ' ' || *pData == '\n' || *pData == '\r')
		{
			pData++;

		}
		else
		{
			break;
		}
	}
	for (int iter = 0; iter < 1000; iter++)
	{	
		str.AppendFormat(_T("%c"), *pData) ;
		pData++;
		if (*pData == ' ' || *pData == '\n' || *pData == '\r')
		{
			
			while (1)
			{
				pData++;
				if (*pData == ' ' || *pData == '\n' || *pData == '\r')
				{
				}
				else
				{
					return SolveProblem2(str);
				}
			}
			
		}
	}
	return strResult;

}
void CCodeJam_WordSortDlg::OnBnClickedTidyNumbers()
{
	CFileDialog dlg(TRUE);
	if (dlg.DoModal() == IDOK)
	{
		CFile f;
		if (f.Open(dlg.GetPathName(), CFile::modeRead))
		{
			int nLength = (int)f.GetLength();
			BYTE *pData = new BYTE[nLength];
			f.Read(pData, nLength);
			int nCount = ReadCount(pData);
			CFile fW;
			if (fW.Open(dlg.GetPathName() + _T(".out"), CFile::modeCreate | CFile::modeWrite))
			{
				for (int iter = 0; iter < nCount; iter++)
				{
					CString strResult = SolveProblem2(pData);
					CString str;
					str.Format(_T("Case #%d: %s\r\n"), iter + 1, strResult);
					
					char chResult[2000];
					strcpy_s(chResult, 2000, CT2A(str));
					int nAnswer = strlen(chResult);
					fW.Write(chResult, nAnswer);
				}
				fW.Close();
			}
		}
	}
}
typedef struct GG
{
	LONGLONG LS;
	LONGLONG RS;
	BOOL bResult;
	GG()
	{
		LS = 0;
		RS = 0;
		bResult = FALSE;

	}

};
GG SolveProblem3(BOOL* p,LONGLONG llRoomCount, LONGLONG llPeopleCount )
{	
	GG gg;
	int nMaxCount = 0;
	int nCount = 0;
	int nIndex = 0;
	for (int iter = 0; iter < llRoomCount; iter++)
	{
		
		if (p[iter])
		{
			if (nMaxCount < nCount)
			{
				nIndex = iter - nCount;
				nMaxCount = nCount;
			}
			nCount = 0;
		}
		else
		{
			nCount++;
			if (nMaxCount < nCount)
			{
				nIndex = iter - nCount;
				nMaxCount = nCount;
			}
		}
	}
	if (nMaxCount)
	{
		gg.LS = (nMaxCount - 1) / 2;
		gg.RS = (nMaxCount - 1) - gg.LS;
		p[nIndex + gg.RS + 1] = TRUE;
	}
	else
	{
		gg.RS = 0;
		gg.LS = 0;
	}
	
	
	return gg;
}
CString SolveProblem3(LONGLONG llRoomCount, LONGLONG llPeopleCount)
{
	/*if ((llRoomCount)/ 2 < llPeopleCount)
		return _T("0 0");*/

	
	LONGLONG temp = llPeopleCount;
	LONGLONG llRoomCountTemp = llRoomCount;
	BOOL bBalanced = TRUE;
	int nCount = 0;
	if (llPeopleCount > 1)
	{
		while (1)
		{


			nCount++;
			if (llPeopleCount <= pow(2, nCount + 1) - 1)
			{
				break;
			}

		}
	}
	
	int nUnBalanceCount = 0;
	int nBalanceCount = 1;
	
	
	
	for (int iter = 0; iter < nCount; iter++)
	{	
		BOOL bUnBalanced = ((llRoomCountTemp-1) % 2 == 1);
		if (bUnBalanced)
		{
			nUnBalanceCount = nUnBalanceCount * 2 + nBalanceCount;
		}
		
		nBalanceCount = pow(2, iter+1) - nUnBalanceCount;

		llRoomCountTemp = ((llRoomCountTemp -1) / 2.0 + 0.5);
	}
	temp = llPeopleCount - (pow(2, nCount) -1);
	
	if(llRoomCountTemp > 0 )
		llRoomCountTemp --;
	if (temp >  nBalanceCount && nBalanceCount>0 && llRoomCountTemp > 0)
	{
		llRoomCountTemp--;
	}
	LONGLONG RS = llRoomCountTemp / 2;
	LONGLONG LS = llRoomCountTemp - RS;
	CString strResult;
	strResult.Format(_T("%lli %lli"), LS, RS);
	
	return strResult;

}
CString SolveProblem3(BYTE*&p)
{
	while (1)
	{
		if (*p == ' ' || *p == '\n' || *p == '\r')
		{
			p++;

		}
		else
		{
			break;
		}
	}
	LONGLONG llRoomCount = ReadCountLongLong(p);
	LONGLONG llPeopleCount = ReadCountLongLong(p);
	/*GG result;
	BOOL* pbool = new BOOL[llRoomCount];
	memset(pbool, 0, sizeof(BOOL)*llRoomCount);
	for (int iter = 0; iter < llPeopleCount; iter++)
	{
		result = SolveProblem3(pbool,llRoomCount, llPeopleCount);
	}
	delete[]pbool;
	CString str;
	str.Format(_T("%lli %lli"), result.RS, result.LS);
	CString strResult;
	strResult = SolveProblem3(llRoomCount, llPeopleCount);
	if (strResult != str)
	{
		SolveProblem3(llRoomCount, llPeopleCount);
	}
		
	strResult.Format(_T("%lli %lli ___ "), llRoomCount, llPeopleCount);
	SolveProblem3(500, 116);
	return strResult + str + _T(" : ") + SolveProblem3(llRoomCount, llPeopleCount);*/
	return SolveProblem3(llRoomCount, llPeopleCount);
	
}
void CCodeJam_WordSortDlg::OnBnClickedBathroomStalls()
{
	CFileDialog dlg(TRUE);
	if (dlg.DoModal() == IDOK)
	{
		CFile f;
		if (f.Open(dlg.GetPathName(), CFile::modeRead))
		{
			int nLength = (int)f.GetLength();
			BYTE *pData = new BYTE[nLength];
			f.Read(pData, nLength);
			int nCount = ReadCount(pData);
			CFile fW;
			if (fW.Open(dlg.GetPathName() + _T(".out"), CFile::modeCreate | CFile::modeWrite))
			{
				for (int iter = 0; iter < nCount; iter++)
				{
					CString strResult = SolveProblem3(pData);
					CString str;
					str.Format(_T("Case #%d: %s\r\n"), iter + 1, strResult);

					char chResult[2000];
					strcpy_s(chResult, 2000, CT2A(str));
					int nAnswer = strlen(chResult);
					fW.Write(chResult, nAnswer);
				}
				fW.Close();
			}
		}
	}
}
