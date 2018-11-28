#include <bits/stdc++.h>

//#define INTER_CHECK
#define A_1
//#define A_2
//#define B_1
//#define B_2

#define BUFSIZE 1000000
char buf[BUFSIZE];

#define MANYTESTS 1
//#define LINEBYLINE 1

using namespace std;

//Scanner Helpers
string
getLine() {
  	string s;
	while(!feof(stdin)) {
		char c = fgetc(stdin);
		if(c <= 0) continue;
		if(c == 13) continue;
		if(c == 10) return s;
	s += c;
	}
	return s;
}

int
getNum() {
#ifdef LINEBYLINE
	string s = getLine();
	return atoi(s.c_str());
#else
	int i;
	scanf("%d", &i);
	return i;
#endif
}

string
getStr() {
#ifdef LINEBYLINE
	return getStr();
#else
	scanf("%s", buf);
	return buf;
#endif
}

long long
getLL()
{
#ifdef LINEBYLINE
	string s = getLine();
	return atoll(s.c_str());
#else
#ifdef USEWIN
	string s = getStr();
	return atoll(s.c_str());
#else
	long long v;
	scanf("%Ld", &v);
	return v;
#endif
#endif
}

//Printer Helpers

void
print_arr_str(string arr,int N)
{
	int itr = 0;

	for (itr = 0; itr < N ; itr++)
	{
		printf("%c, ",arr[itr]);
	}
	printf("\n");
}

void
print_arr_int(int *arr,int N)
{
	int itr = 0;

	for (itr = 0; itr < N ; itr++)
	{
		printf("%d, ",arr[itr]);
	}
	printf("\n");
}

//list, stack and queue related APIs
//set and map APIs
//unordered set and unordered map APIS

bool
fncomp(long long lhs, long long rhs)
{
	return rhs<lhs; // for decreasing seq
}
bool
fncomp2(double lhs, double rhs)
{
	return rhs<lhs; // for decreasing seq
}

void
print_map(map<long long, long long, bool (*)(long long, long long)> mymap)
{
	map<long long,long long>::iterator myitr = mymap.begin();

	while(myitr != mymap.end())
	{
		cout << "(" << myitr->first << "==" << myitr->second << ")";
		myitr++;
	}
}

void
print_set(set<double, bool(*)(double, double)> myset)
{
	set<double, bool(*)(double, double)>::iterator myitr = myset.begin();

	while (myitr!=myset.end())
	{
		cout << *myitr << " ";
		myitr++;
	}
	cout << "\n";
}

void _main(int TEST)
{
	//string str = getStr();
	//int len = str.length();
	//print_arr_str(str, len);
	long long D = getLL();
	double hrs = 0;
	int N = getNum();
	int itr = 0;
	bool (*fnptr)(long long, long long) = fncomp;
	bool (*fnptr2)(double, double) = fncomp2;
	map<long long, long long, bool(*)(long long, long long)> mymap(fnptr);
	long long K[1000];
	long long S[1000];

	set<double, bool(*)(double, double)> myset(fnptr2);

	for (itr = 0; itr < N; itr++)
	{
		K[itr] = getLL();
		S[itr] = getLL();

		hrs = (double)(D - K[itr])/(double)S[itr];
		//cout << K[itr] <<" " <<  S[itr] << "\n";
		//mymap.insert(pair<long long, long long>(K[itr], S[itr]));
		myset.insert(hrs);
	}

	set<double, bool(*)(double, double)>::iterator myitr = myset.begin();
	hrs = *myitr;

	double Res = (double)D/(double)hrs;
	cout << fixed << setprecision(6);
	cout << Res << "\n";
	//print_set(myset);
}

int main()
{

#ifdef A_1  
    	freopen("A-small-attempt0.in", "r", stdin);
    	freopen("A-small-attempt0.out", "w", stdout);
#endif
#ifdef A_2
	freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
#endif
#ifdef B_1
        freopen("B-small-attempt0.in", "r", stdin);
        freopen("B-small-attempt0.out", "w", stdout);
#endif
#ifdef B_2
        freopen("B-large.in", "r", stdin);
        freopen("B-large.out", "w", stdout);
#endif
#ifdef INTER_CHECK
	freopen("file.txt", "r", stdin);
#endif
	int TEST;

	if (!MANYTESTS)
		TEST = 1;
	else
		TEST = getNum();

    	for(int i=1; i<=TEST; i++)
    	{
        	printf("Case #%d: ", i);
        	_main(i);
    	}
    	return 0;
}
