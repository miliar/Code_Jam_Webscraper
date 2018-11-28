#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>
#include <iomanip>
#include <time.h>

using namespace std;

void testing (int position = 0){static clock_t clock_tStart;if (position==0){freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);clock_tStart = clock();}else {printf("\n\nTime taken: %fs\n\n", (double)(clock() - clock_tStart)/CLOCKS_PER_SEC);}}
void real_main();
int main ()
{
#ifdef WINDORO
testing(0);
#endif
    real_main();
#ifdef WINDORO
testing(1);
#endif
    return 0;
}
// --------------------------------- CODE HERE ------------------------------------------ 

#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 2000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;

int angka[50];
int l_angka;
int posisi_salah_angka;

bool isValid()
{
    for (int i=1;i<l_angka;i++)
    {
        if ( angka[i-1] > angka[i] )
        {
            posisi_salah_angka = i-1;
            return false;
        }
    }
    return true;
}

void real_main(){
	int t;
    cin >> t;
    for (int kasus=1;kasus<=t;kasus++)
    {
        string s;
        cin >> s;
        for (int i=0;i<50;i++)angka[i] = 0;
        for (int i=0;i<s.size();i++ )
        {
            angka[i] = s[i] - '0';
        }
        l_angka = s.size();
        
        while (!isValid())
        {
            angka[posisi_salah_angka]--;
            for (int i=posisi_salah_angka+1;i<l_angka;i++) angka[i] = 9;
            
            if (angka[0]==0)
            {
                for (int i=1;i<l_angka;i++)
                {
                    angka[i-1] = angka[i];
                }
                l_angka--;
            }
        }
        
        cout << "Case #"<< kasus <<": ";
        for (int i=0;i<l_angka;i++)cout << angka[i]; cout << endl;
    }
	
}













