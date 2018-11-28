// GoogleJam_Problem1.cpp : Defines the entry point for the console application.
//

//#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS

#include "stdafx.h"
#include "StringHelpers.h"
#include "windows.h"
#include <queue>
#include <xmmintrin.h>
 

//vector<long long> ix;

__declspec(thread) char * g_hash = NULL; 
size_t g_hashSize = 10 * 1024 * 1024;
vector<string> g_l;
volatile unsigned int g_lc = 0;
volatile unsigned int g_curOut = 1;
HANDLE g_ParametersParsedEvent = NULL;
FILE * g_fout = NULL;

//std::hash_map<unsigned long long, long long> g_h;

class Cmp
{
public:
    bool operator()(long l, long r) const
    {
        return r < l;
    }
};

struct Point
{
    Point() : x(0), y(0), id(0)  {};
    Point(long long x1, long long y1, int id1) : x(x1), y(y1), id(id1)  {};

    long long x;
    long long y;
    int id;
};

double g_a[103][103];
double g_p[103][103]; 
//char g_os[20][100][3];
//
//int g_numo[20] = { 0, 1, 2, 6, 100 };


VLL g_primes;
long long g_maxp;

long long GetDivisor(long long t)
{
	long long mp = (long long)sqrt(t);

	for (unsigned int i = 0; i < g_primes.size(); ++i)
	{
		long long p = g_primes[i];
		if (t % p == 0)
			return p;
		if (p > mp)
			return 0;
	}

	return 0;
}


bool IsPrimeNew(long long t)
{
	if (t < g_maxp)
	{
		// use array
		return ((*(g_hash + t / 8)) & (1 << (t&0x7))) != 0;
	}
	else
	{
		long long d = GetDivisor(t);
		return d == 0;
	}
}


void getPrimes(long long m, VLL &vp, char * phash)
{
	memset(phash, 0, (size_t)m / 8 + 1);

	long long l = (long long)(sqrt(m)) + 1;
	vp.reserve((size_t)l);
	vp.push_back(2);
	*(phash + 2 / 8) |= (1 << (2 & 0x7));

	for (long long i = 3; i <= m; i += 2)
	{
		unsigned int j = 0;
		bool good = true;
		for (; j < vp.size(); ++j)
		{
			long long p = vp[j];
			if (i % p == 0)
			{
				good = false;
				break;
			}

			if (p * (long long)p > i)
				break;
		}

		if (good)
		{
		    vp.push_back(i);
			*(phash + i/8) |= (1 << (i&0x7));
		}
	}

	g_maxp = m;
}

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Node {

public:
	Node()
	{
		s = 0;
		c = 0;
	}

	Node(int length, ULL start)
	{
		c = length;
		s = start;
	}

	unsigned c;
	ULL s;
};

class NodeCmp
{
public:
	bool operator()(const Node& ref1, const Node& ref2) const
	{
		if (ref1.c != ref2.c)
		{
			return ref1.c < ref2.c;
		}
		else
		{
			return ref1.s > ref2.s;
		}
	}
};

int SolveSmall(const VI& r, const MI &m)
{
	int res = 0;



	return 0;
}

class SegmentCmp
{
public:
	bool operator()(const ULL& ref1, const ULL& ref2) const
	{
		return ref1 > ref2;
	}
};

typedef LL MPP[51];



double SolveLarge(int n, int k, MI &m)
{
	double res = 0;
	double pi = 3.141592653589793238462643383279;
	ULL r = 0;

	VULL v;

	//vector<Node> v;
	//FOR(i, 0, n)
	//{
	//	vn[i].c = m1[i][0];
	//	vn[i].s = m1[i][1];

	//}

	//sort(vn.begin(), vn.end(), NodeCmp());

	//MI m;

	//int prevr = 0;
	//FOR(i, 0, n)
	//{
	//	if (prevr == m1[i][0])
	//		continue;
	//	m.push_back(m1[i]);
	//	prevr = m1[i][0];
	//}

	//n = m.size();

	FOR(j, 0, n)
	{
		ULL minr = m[j][0];
		int minrh = m[j][1];


		bool took = false;
		v.clear();
		FOR(i, 0, m.size())
		{
			if (m[i][0] <= minr)
			{
				if (i == j)
				{
					continue;
				}
				else
				{
					v.push_back(m[i][1]*(ULL)m[i][0]);
				}
			}
		}

		if (v.size() < (k - 1))
			continue;

		sort(v.begin(), v.end());

		ULL s = minr * minrh;
		FOR(i, v.size() - (k - 1), v.size())
		{
			s += v[i];
		}

		ULL w = minr * minr + 2 * s;
		if (w > r)
			r = w;
	}

	res = pi * r;
	return res;
}

void Test()
{
}

void Init()
{

}

/////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

VOID CALLBACK MyWorkCallback(PTP_CALLBACK_INSTANCE Instance, PVOID Parameter, PTP_WORK Work)
{
	if (g_hash == NULL)
	{
		g_hash = (char *)VirtualAlloc((LPVOID)NULL, g_hashSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	}

	//memset(g_hash, 0, g_hashSize);

	unsigned t = static_cast<unsigned>((unsigned long long)Parameter);

	//printf("Solving %d\n", (int)Parameter);

	// Parsing params
	//

	//string s = g_l[g_lc++];
	VI v = splitInt(g_l[g_lc++]);
	//VI r = splitInt(g_l[g_lc++]);
	
	MI m(v[0]);

	FOR(i, 0, m.size())
	{
		m[i] = splitInt(g_l[g_lc++]);
	}
	//int k = atoi(v1[1].c_str());
	//string s = v1[0];

	SetEvent(g_ParametersParsedEvent);

	// Solving
	//

	//fprintf(g_fout, "Case #%d:", t);
	//fprintf(g_fout, "\n");

	//std::pair<unsigned __int64, unsigned __int64> res;
	// ULL res = 0;
	double res;

	//for (unsigned __int64 i = 0; i < 1000000; ++i)
	//{
	//	_ui64toa_s(i, buf, sizeof(buf), 10);
	//	s.assign(buf);
	//	res = SolveLarge(s);
	//	string res1 = SolveSmall(s);

	//	if (res != res1)
	//	{
	//		printf("Error\n");
	//		res = SolveLarge(s);
	//	}
	//}

	res = SolveLarge(v[0], v[1], m);
	// std::pair<unsigned __int64, unsigned __int64> res1 = SolveSmall(v[0], v[1]);
	//if (res1 != res)
	//{
	//	printf("Error\n");
	//	res = SolveLarge(v[0], v[1]);
	//}

	while (g_curOut != t)
	{
		Sleep(100);
	}

	// Output results
	//

	//char buf[200];
	//sprintf(buf, "Case #%%d: %%0%dI64d %%0%dI64d\n", nn, nn);

	fprintf(g_fout, "Case #%d: %f\n", t, res);
	//FOR(i, 0, res.size())
	//{
	//	fprintf(g_fout, "%s\n", res[i].c_str());
	//}

	//if (res >= 0)
	//{
	//	fprintf(g_fout, "Case #%d: %d\n", t, (int)res);
	//}
	//else
	//{
	//	fprintf(g_fout, "Case #%d: IMPOSSIBLE\n", t);
	//}

	//std::sort(vr, vr + nn);
	//FOR(j, 0, vr.size())
	//{
	//	int r = vr[j];
	//	fprintf(g_fout, "%d %d %d\n", r / 100 + 1, (r / 10) % 10 + 1, r % 10  +1);
	//}
	//fprintf(g_fout, "\n");

	//printf("Solved %d\n", (int)Parameter);
	InterlockedIncrement(&g_curOut);
}

TP_CALLBACK_ENVIRON g_CallBackEnviron;
PTP_POOL g_pool = NULL;

DWORD CreateCustomThreadpool(unsigned int numThreads = 8)
{
	BOOL bRet = FALSE;
	PTP_WORK work = NULL;
	PTP_CLEANUP_GROUP cleanupgroup = NULL;

	InitializeThreadpoolEnvironment(&g_CallBackEnviron);

	// Create a custom, dedicated thread pool.
	g_pool = CreateThreadpool(NULL);

	if (NULL == g_pool) {
		_tprintf(_T("CreateThreadpool failed. LastError: %u\n"), GetLastError());
		return -1;
	}

	// The thread pool is made persistent simply by setting
	// both the minimum and maximum threads to 1.
	SetThreadpoolThreadMaximum(g_pool, numThreads);

	bRet = SetThreadpoolThreadMinimum(g_pool, numThreads);
	if (FALSE == bRet) {
		_tprintf(_T("SetThreadpoolThreadMinimum failed. LastError: %u\n"), GetLastError());
		return -1;
	}

	// Create a cleanup group for this thread pool.
	cleanupgroup = CreateThreadpoolCleanupGroup();
	if (NULL == cleanupgroup) {
		_tprintf(_T("CreateThreadpoolCleanupGroup failed. LastError: %u\n"),  GetLastError());
		return -1;
	}

	// Associate the callback environment with our thread pool.
	SetThreadpoolCallbackPool(&g_CallBackEnviron, g_pool);

	// Associate the cleanup group with our thread pool.
	// Objects created with the same callback environment
	// as the cleanup group become members of the cleanup group.
	SetThreadpoolCallbackCleanupGroup(&g_CallBackEnviron, cleanupgroup, NULL);

	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
    __int64 start = GetTickCount64();
	bool useMultipleThreads = false;

	g_ParametersParsedEvent = CreateEvent(NULL, FALSE, FALSE, NULL);

    char * outPath = "D:\\progs\\GoogleJam_Problem1\\out.txt";

    if(argc < 2)
    {
        printf("Error. Need in and out files\n");
        return -1;
    }

    if (argc >= 3)
    {
        outPath = argv[2];
    }

	if (argc >= 4)
	{
		if (_stricmp(argv[3], "multi") == 0)
		{
			useMultipleThreads = true;
		}
		else
		{
			useMultipleThreads = false;
		}
	}

    FILE * fin = NULL;

    g_fout = _fsopen(outPath, "w", _SH_DENYNO);
    if(g_fout == NULL)
    {
        printf("Can't open %s\n", outPath);
        return -1;
    }

    g_l = fileToLines(argv[1]);
    if (g_l.size() == 0)
    {
        printf("Can't open %s\n", argv[1]);
        return -1;
    }
    int numTests = atoi(g_l[g_lc++].c_str());

    Init();

	if(useMultipleThreads)
		CreateCustomThreadpool(8);
	// getPrimes((1ll << 19) - 1, g_primes, g_hash);

	Test();

	for(int t = 1; t <= numTests; ++t)
    {
		if (!useMultipleThreads)
		{
			MyWorkCallback(NULL, (void *)(unsigned long long)t, NULL);
		}
		else
		{
			// Create work with the callback environment.
			PTP_WORK work = CreateThreadpoolWork(MyWorkCallback, (PVOID)(unsigned long long)t, &g_CallBackEnviron);
			if (work == NULL) printf("ERROR: failed to create work item, 0x%x\n", GetLastError());
			SubmitThreadpoolWork(work);
			while(WaitForSingleObject(g_ParametersParsedEvent, INFINITE) != WAIT_OBJECT_0);
		}
    }

	while (g_curOut != numTests + 1)
	{
		Sleep(100);
	}

    fclose(g_fout);

    __int64 end = GetTickCount64();

    printf("Time = %.3f sec\n", ((double)(end - start))/1000);

    return 0;
}

