// A.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"

#include <map>
#include <set>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cassert>
#include <math.h>

using namespace std;
#include <windows.h>
//#define PROC_NUM 8
bool bDoIt = true;////MULTIPROC
bool RunMultiProc(int argc, _TCHAR* argv[]);
char outName[100] = "out.txt";
int fromProblem = -1, fromProblemNext = INT_MAX;
int theCase;
int totalCases;

ifstream in("C-small-2-attempt0.in");
ofstream out;
///LLONG_MAX,INT_MA
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 
#define amfor(Iterator, Container) 	for ( auto Iterator = begin(Container); (Iterator) != end(Container); ++(Iterator) )
#define ramfor(Iterator, Container) for ( auto Iterator = Container.rbegin(); (Iterator) != Container.rend(); ++(Iterator) )
template<class C, class E> inline bool contains(const C& container, const E& element) { return container.find(element) != container.end(); }
#define  NP(nn,ta,a,tb,b) struct nn : pair<ta,tb> { nn():pair<ta,tb>(){}; nn(ta pa,tb pb):pair<ta,tb>(pa,pb){} ta& a(){return first;} tb& b(){return second;} };
template<class T> inline void checkmin(T &a, T b) { if (b < a) a = b; }//asigna en a el minimo
template<class T> inline void checkmax(T &a, T b) { if (b > a) a = b; }//asigna en a el maximo
///typedef ttmath::Int<10> ii;

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))

///typedef ttmath::Int<10> II;///640 bits
typedef __int64 II;
//typedef ttmath::Big<1,10> DD;/// 64 exp ,640bits mant
typedef double DD;
#define INF LLONG_MAX

int N, K;

pair<int, int> S(int nn, int kk)
{
	assert(kk > 0);
	if (kk == 1)
	{
		if (nn % 2 == 1)
		{
			return mp(nn / 2, nn / 2);
		}
		else
		{
			return mp(nn / 2, nn / 2-1);
		}
	}
	kk--;
	if (nn % 2 == 1)
	{///nn/2 y nn/2
		return S(nn/2,(kk+1)/ 2);
	}
	else
	{///nn/2 y nn/2-1
		if (kk % 2 == 0)
			return S(nn / 2 - 1, kk / 2);///igual a ambos ultimo el menor
		else
			return S(nn/2,kk/2+1);//sobra uno arranca en el mas grande
	}

}

void Solve()
{
	in >> N >> K;
	if (!bDoIt)
		return;
	pair<int, int> res = S(N, K);
	out << res.first<<" "<< res.second;
}
int _tmain(int argc, _TCHAR* argv[])
{
	in >> totalCases;
	if(RunMultiProc(argc, argv))
		return 0;
	out.open(outName);
	//out.open("out.txt");
	out << std::fixed;
	for(theCase = 0;theCase < totalCases;theCase++)
	{
		bDoIt = (theCase >= fromProblem && theCase < fromProblemNext);
		if(bDoIt){cout << theCase << endl; out << "Case #" << theCase+1 << ": ";	}
		Solve();
		if(bDoIt)out << endl;
	}	
	return 0;
}


bool RunMultiProc(int argc, _TCHAR* argv[])
{
#ifdef PROC_NUM
	if(argc == 1)
	{
		cout << "TOTAL " << totalCases << endl;
		CreateDirectory(L"Tmp",NULL);
		PROCESS_INFORMATION procInfo[PROC_NUM];
		HANDLE waits[PROC_NUM];
		STARTUPINFO s;
		memset(&s,0,sizeof(s));
		REP(i,PROC_NUM )
		{
			s.cb = sizeof(s);
			_TCHAR appExe[1000];
			wsprintf(appExe,L"%s %d",argv[0],i);
			CreateProcess(NULL,appExe,NULL,NULL,FALSE,0,NULL,NULL,&s,&procInfo[i]);
			waits[i] = procInfo[i].hProcess;
		}
		WaitForMultipleObjects(PROC_NUM,waits,TRUE,INFINITE);
		out.open("out.txt");
		REP(i,PROC_NUM)
		{
			char inName[100];
			sprintf(inName,"Tmp\\out%d.txt",i);
			ifstream tmpIn(inName);
			char line[10000];
			while(!tmpIn.getline(line,10000).fail())
				out << line << endl;
		}
		return true;
	}
	int thisProc;
	swscanf(argv[1],L"%d",&thisProc);
	int probPerProc = totalCases/PROC_NUM;
	if(totalCases%PROC_NUM != 0)
		++probPerProc;
	fromProblem = thisProc*probPerProc;fromProblemNext = (thisProc+1)*probPerProc;
	sprintf(outName,"Tmp\\out%d.txt",thisProc);
#endif
	return false;
}
