// B.cpp : Defines the entry point for the console application.
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

ifstream in("B-large.in");
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

int Ac,Aj;
///0 = c 1 = j
bool act[2][1440];
const int CAM = 0;
const int JAM = 1;


int Other(int index)
{
	return 1 - index;
}

#define INV 1000000000

int TestStartingAt(int index)
{
	if (act[index][0])
		return INV;///no se puede
	///[quien lo tenia][horas cameron]
	int excTmpHorasCameron[2][1441];
	int newExcTmpHorasCameron[2][1441];
	///Barriendo solo primer min


	FOR(i, 0, 1440)
		excTmpHorasCameron[CAM][i] = excTmpHorasCameron[JAM][i] = INV;///imp
																	  //arranca con index
	if (index == CAM)
	{///arranca CAM
		excTmpHorasCameron[CAM][1] = 0;///el primero se lo doy a CAM index no exchange.
		///el resto no es posible
	}
	else
		excTmpHorasCameron[JAM][0] = 0;///el primero se lo doy a JAM index no exchange.

// 	int other = Other(index);
// 	///Termina en JAM
// 	if (act[other][0])
// 		excTmpHorasCameron[other][1] = INV;
// 	else
// 		excTmpHorasCameron[other][1] = (other == CAM) ? 1 : 0;;
	///No es posible que CAM tenga mas d
	FOR(i,1,1439)///agrego minuto i
	{
		FOR(j,0,1440)
		{///miro toda carga si se lo queda CAM. Lleno la mejor manera de que CAM tenga j horas y se lo quede
			if (act[CAM][i])
				newExcTmpHorasCameron[CAM][j] = INV;//no puede
			else
			{///si se lo queda CAM y tiene j es porque CAM viene de tener j-1
				if(j == 0)
					newExcTmpHorasCameron[CAM][j] = INV;//no puede no tener horas
				else
				{
					int v1 = INV,v2 = INV;
					if (excTmpHorasCameron[CAM][j - 1] != INV)///lo tenia ella
						v1 = excTmpHorasCameron[CAM][j - 1];
					if (excTmpHorasCameron[JAM][j - 1] != INV)///lo tenia JAM
						v2 = excTmpHorasCameron[JAM][j - 1]+1;
					assert(v1 >= 0);
					assert(v2 >= 0);
					newExcTmpHorasCameron[CAM][j] = min(v1, v2);
				}
			}

			if (act[JAM][i])
				newExcTmpHorasCameron[JAM][j] = INV;//no puede
			else
			{///si se lo queda JAM y CAM tiene J es porque CAM viene de tener j
				int v1 = INV, v2 = INV;
				if (excTmpHorasCameron[JAM][j] != INV)///lo tenia JAM
					v1 = excTmpHorasCameron[JAM][j];//o sigue tienuendo JAM
				if (excTmpHorasCameron[CAM][j] != INV)///lo tenia CAM
					v2 = excTmpHorasCameron[CAM][j] + 1;//lo tiene JAM
				assert(v1 >= 0);
				assert(v2 >= 0);
				newExcTmpHorasCameron[JAM][j] = min(v1, v2);
			}
		}
		swap(excTmpHorasCameron, newExcTmpHorasCameron);
	}
	return min(excTmpHorasCameron[CAM][720] + ((index != CAM)?1:0), excTmpHorasCameron[JAM][720] + ((index != JAM) ? 1 : 0));
}

void Solve()
{
	in >> Ac>>Aj;
	REP(i, 1440)
		act[0][i] = act[1][i] = false;
	REP(i, Ac)
	{
		int c, d;
		in >> c >> d;
		REP(j, d-c)
		{
			assert(c + j < 1440);
			act[CAM][c + j] = true;
		}
	}
	REP(i, Aj)
	{
		int c, d;
		in >> c >> d;
		REP(j, d-c)
		{
			assert(c + j < 1440);
			act[JAM][c + j] = true;
		}
	}
	if(!bDoIt)
		return;


	int v1 = TestStartingAt(0);
	int v2 = TestStartingAt(1);
	int res = min(v1, v2);
	assert(res != INV);
	out << res;
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
