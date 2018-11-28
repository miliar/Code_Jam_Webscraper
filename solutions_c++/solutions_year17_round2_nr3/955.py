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
#include <limits>
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

ifstream in("C-large.in");
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

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))

///typedef ttmath::Int<10> II;///640 bits
typedef __int64 II;
//typedef ttmath::Big<1,10> DD;/// 64 exp ,640bits mant
typedef double DD;
#define INF LLONG_MAX

int N,Q;
#define MAX 101

__int64 graph[MAX][MAX];
__int64 allDistances[MAX][MAX];
///salogo de i a j
double allTimes[MAX][MAX];

double allMinTimes[MAX][MAX];

struct Horse
{
	__int64 _dist;
	__int64 _speed;
};
vector<Horse> horses;
#define INF LLONG_MAX
#undef max
const double DINF = (std::numeric_limits<double>::max());

void ShowData1()
{
	return;
	cout << "Dist" << endl;
	REP(i, N)
	{
		REP(j, N)
		{
			cout << allDistances[j][i] << " ";
		}
		cout << endl;
	}
	cout << "=================" << endl;

}
void ShowData2()
{
	return;
	cout << "Dist2" << endl;
	REP(i, N)
	{
		REP(j, N)
		{
			cout << allMinTimes[j][i] << " ";
		}
		cout << endl;
	}
	cout << "=================" << endl;

}
void ShortestAll1()
{
	REP(i, N)
	{
		REP(j, N)
		{
			if (i != j)
				allDistances[i][j] = graph[i][j];
			else
				allDistances[i][j] = 0;
		}
	}
	ShowData1();
	REP(k, N)
	{
		REP(i, N)
		{
			REP(j, N)
			{
				if (allDistances[i][k] != INF && allDistances[k][j] != INF)
				{
					__int64 newDist = allDistances[i][k] + allDistances[k][j];
					if (newDist < allDistances[i][j])
					{
						allDistances[i][j] = newDist;
					}
				}
			}
		}
	}
}
void ShortestAll2()
{
	REP(i, N)
	{
		REP(j, N)
		{
			if (i != j)
				allMinTimes[i][j] = allTimes[i][j];
			else
				allMinTimes[i][j] = 0;
		}
	}
	ShowData2();
	//	ShowData();
	REP(k, N)
	{
		REP(i, N)
		{
			REP(j, N)
			{
				if (allMinTimes[i][k] != DINF && allMinTimes[k][j] != DINF)
				{
					double newTime = allMinTimes[i][k] + allMinTimes[k][j];
					if (newTime < allMinTimes[i][j])
					{
						allMinTimes[i][j] = newTime;
					}
				}
			}
		}
	}
}

void Solve()
{
	in >> N >> Q;
	if (!bDoIt)
		return;
	horses.resize(N);
	REP(i, N)
	{
		in >> horses[i]._dist;
		in >> horses[i]._speed;
	}
	REP(i, N)
	{
		REP(j, N)
		{
			in >> graph[i][j];
			if (graph[i][j] == -1)
				graph[i][j] = INF;
		}
	}
	ShortestAll1();
	ShowData1();
	REP(i, N)
	{
		REP(j, N)
		{
			if (allDistances[i][j] == INF)
				allTimes[i][j] = DINF;
			else
			{
				if(allDistances[i][j] > horses[i]._dist)
					allTimes[i][j] = DINF;
				else
					allTimes[i][j] = (double)allDistances[i][j]/(double)horses[i]._speed;
			}
		}
	}
	ShortestAll2();
	ShowData2();
	REP(i, Q)
	{
		int from, to;
		in >> from >> to;
		--from;
		--to;
		out << allMinTimes[from][to] << " ";
	}
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
