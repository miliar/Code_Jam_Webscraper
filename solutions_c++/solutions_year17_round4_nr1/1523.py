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
//http://www.ttmath.org/
#include "ttmath\ttmath.h"

using namespace std;
#include <windows.h>
//#define PROC_NUM 8
bool bDoIt = true;////MULTIPROC
bool RunMultiProc(int argc, _TCHAR* argv[]);
char outName[100] = "out.txt";
int fromProblem = -1, fromProblemNext = INT_MAX;
int theCase;
int totalCases;

ifstream in("A-large.in");
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
template<class C, class E> inline bool contains(const C& container, const E& element){	return container.find(element) != container.end() ;}
#define  NP(nn,ta,a,tb,b) struct nn : pair<ta,tb> { nn():pair<ta,tb>(){}; nn(ta pa,tb pb):pair<ta,tb>(pa,pb){} ta& a(){return first;} tb& b(){return second;} };
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//asigna en a el minimo
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//asigna en a el maximo
///typedef ttmath::Int<10> ii;

#undef max
#undef min

// #define max(a,b)            (((a) > (b)) ? (a) : (b))
// #define min(a,b)            (((a) < (b)) ? (a) : (b))

///typedef ttmath::Int<10> II;///640 bits
typedef __int64 II;
//typedef ttmath::Big<1,10> DD;/// 64 exp ,640bits mant
typedef double DD;
#define INF LLONG_MAX

int N,P;
vector<int> g;

void Solve2()
{
	int cimp = 0;
	REP(i,N)
	{
		if (g[i] % 2 == 1)
			++cimp;
	}
	out << N-(cimp / 2);
}
void Solve3()
{
	int v[4];
	REP(i, P)
		v[i] = 0;
	REP(i, N)
		v[g[i] % P]++;
	int res = 0;
	res += min(v[1], v[2]);
	v[1] -= res;
	v[2] -= res;
	if(v[2] != 0)
	{
		int commenBien = (((v[2] - 1) / 3) + 1);
		assert(commenBien <= v[2]);
		int commenMal = v[2] - commenBien;
		res += commenMal;
	}
	else if(v[1] != 0)
	{ 
		int commenBien = (((v[1] - 1) / 3) + 1);
		assert(commenBien <= v[1]);
		int commenMal = v[1] - commenBien;
		
		res += commenMal;
	}
	assert(res <= N);
	out << N-res;

}
void Solve4()
{
	int res = 0;
	int v[4];
	REP(i, P)
		v[i] = 0;
	REP(i, N)
		v[g[i] % P]++;
	res += min(v[1], v[3]);
	v[1] -= res;
	v[3] -= res;
	if (v[3] != 0)
	{///solo 3 y 2
		int mal2 = v[2] / 2;
		res += mal2;
		v[2] -= mal2*2;

		int pos = v[2]*2;
		while (v[3] != 0)
		{
			if (pos % 4 != 0)
				res++;
			v[3]--;
			pos++;
		}
	}
	else
	{///solo 1 y 2 
		int mal2 = v[2] / 2;//junto los 2
		res += mal2;
		v[2] -= mal2 * 2;
		int pos = v[2] * 2;
		while (v[1] != 0)
		{
			if (pos % 4 != 0)
				res++;
			v[1]--;
			pos++;
		}
	}
	out << N - res;
}


void Solve()
{
	in >> N >> P;
	g.resize(N);
	REP(i, N)
		in >> g[i];

	if(!bDoIt)
		return;
	if (P == 2)
		Solve2();
	else if (P == 3)
		Solve3();
	else
		Solve4();

	//	out << n;
}
typedef ttmath::Big<2, 256> MyDouble;
int _tmain(int argc, _TCHAR* argv[])
{
	in >> totalCases;
	if(RunMultiProc(argc, argv))
		return 0;
	out.open(outName);
	//out.open("out.txt");
	out << std::setprecision(15);
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
