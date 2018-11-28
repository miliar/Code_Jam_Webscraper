#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <list>

using namespace std;
typedef  long long ll;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputt.txt", "w", stdout);

    int c;
    cin>>c;
    for (int ii = 0 ; ii<c; ii++) {
        cout<<"Case #"<<ii+1<<": ";
        string s;
        cin>>s;
        int n ;
        cin>>n;
        int sol = 0 ;
        
        for (int i =0; i<s.length()-n+1; i++) {
            if(s[i]=='-'){
                for (int j = i; j<i+n; j++) {
                   if(s[j]=='-') s[j]='+';
                   else if(s[j]=='+') s[j]='-';
                }
                sol++;
            }
        }
        for (int i =0; i<s.length(); i++) {
            if (s[i]=='-') {
                sol=-1;
                break;
            }
        }
        if(sol!=-1)cout<<sol<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
 
    return 0;
}

