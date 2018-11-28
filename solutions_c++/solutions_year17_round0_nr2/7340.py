/*
    *
    * Cyrus Jackson
    * VIT University - India
    *
*/
#define TCase(k) cout<<"Case #"<<(int)k+1<<": ";
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory.h>
#include <cassert>
#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <functional>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <time.h>
#include <stack>
#include <set>
#define cl1 double _time=clock();
#define cl2 cout<<"time: "<<double(clock()-_time);
#define BO ios_base::sync_with_stdio(false); cin.tie(NULL)
#define fi BO;freopen("in.txt","r",stdin);
#define fo freopen("out.txt", "w", stdout);
#define test()    int test_case;cin>>test_case;while(test_case--)
 
#define forR(i,n) for (int i = n; i --> 0; )
#define forO(i,n) for(int i = 1; i <= n; i++)
#define forN(i,n) for(int i = 0; i < n; i++)
#define forA(i,a,n) for(int i = a; i < n; i++)
#define s(t) scanf("%d",&t)

#define fill(t) memset(t,0,sizeof(t));
typedef long long int ll;
int GCD(int A, int B) {    if(B==0)        return A;    else        return GCD(B, A % B); }

int MOD = 1e9 + 7;
const int INF = 1<<29;
#define MAX 11111
using namespace std;


string solve(string s){
    int n = s.length();
    if(n <= 1) 
        return s;
    int pos = -1;
    s[n-1] -= 1;
   forR(i,n){
       if(s[i] < s[i-1]){
       pos = i;
    //   if(s[i] == '0' and i > 1) s[i-1] = '9';
    //   cout<<s<<" -"<<endl;
       }
   }
   pos--;
   if(pos == 0){
       forN(i,n) if(i == 0) s[i] -= 1;
       else 
       s[i] = '9';
   }
   else if(pos > 0){
       forN(i,n){
           if(i == pos){
               s[i] -= 1;
               if(s[i] == '0'){
                   int tt = i;
                   while(tt>0){
                       s[tt] = '9';
                       s[tt-1] = '0';
                       tt--;
                   }
           }
           }
           else if(i > pos) s[i] = '9';
       }
   }
   if(s[0] == '9')
   {
       s[0] = '8';
       forO(i,n-1)
       s[i] = '9';
   }
   
    s.erase(0, s.find_first_not_of('0'));
    return s;
}
int main(){
  // fi;fo;
  int testCase = 0;
    test(){
        string s;
        cin>>s;
        TCase(testCase);
        cout<<solve(s);
        cout<<endl;
        testCase++;
    }
    return 0;
}
/*
    *
    * Cyrus Jackson
    * VIT University - India
    *
*/
#define TCase(k) cout<<"Case #"<<(int)k+1<<": ";
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory.h>
#include <cassert>
#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <functional>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <time.h>
#include <stack>
#include <set>
#define cl1 double _time=clock();
#define cl2 cout<<"time: "<<double(clock()-_time);
#define BO ios_base::sync_with_stdio(false); cin.tie(NULL)
#define fi BO;freopen("in.txt","r",stdin);
#define fo freopen("out.txt", "w", stdout);
#define test()    int test_case;cin>>test_case;while(test_case--)
 
#define forR(i,n) for (int i = n; i --> 0; )
#define forO(i,n) for(int i = 1; i <= n; i++)
#define forN(i,n) for(int i = 0; i < n; i++)
#define forA(i,a,n) for(int i = a; i < n; i++)
#define s(t) scanf("%d",&t)

#define fill(t) memset(t,0,sizeof(t));
typedef long long int ll;
int GCD(int A, int B) {    if(B==0)        return A;    else        return GCD(B, A % B); }

int MOD = 1e9 + 7;
const int INF = 1<<29;
#define MAX 11111
using namespace std;


string solve(string s){
    int n = s.length();
    if(n <= 1) 
        return s;
   forR(i,n){
       if(s[i] < s[i-1]){
     s[i-1] -= 1;
     forA(j,i,n) s[j] = '9';
       }
   }
  
    s.erase(0, s.find_first_not_of('0'));
    return s;
}
int main(){
//   fi;fo;
  int testCase = 0;
    test(){
        string s;
        cin>>s;
        TCase(testCase);
        cout<<solve(s);
        cout<<endl;
        testCase++;
    }
    return 0;
}
