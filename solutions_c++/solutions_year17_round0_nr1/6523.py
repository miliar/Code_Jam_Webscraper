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

void real_main(){
	int t;
    cin >> t;
    
    for (int kasus = 1;kasus<=t;kasus++)
    {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        
        for (int i=0;i<s.size();i++)
        {
            if (s[i] == '+')continue;
            if ( i + k > s.size() )
            {
                ans = -1;
                break;
            }
            ans++;
            for (int j=i, l=0;l<k;l++,j++)
            {
                if (s[j] == '+')s[j] = '-';
                else s[j] = '+';
            }
        }
        
        cout << "Case #"<< kasus <<": ";
        if (ans == -1)cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
	
	
	
}













