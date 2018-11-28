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
#include <sstream>  // Required for stringstreams

using namespace std;
typedef   long long ll;


int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("outputcodesmallB.txt", "w", stdout);

    int cases = 0 ;
    cin>>cases;
    for (int kk = 1; kk<cases+1; kk++) {
        int N, R, O, Y, G, B,V;
        cin>>N>>R>>O>>Y>>G>>B>>V;

        int a[3]={0,0,0};
        a[0]=R;
        a[1]=B;
        a[2]=Y;
        string s="";
        if(a[0]) {s+="R";a[0]--;}
        else if(a[1]) {s+="B";a[1]--;}
        else if(a[2]) {s+="Y";a[2]--;}
        int impo=0;
        while (a[0]+a[1]+a[2]!=0) {
            
            if (s[s.length()-1]=='R') {
              //  cout<<s<<"  ** "<<a[1]<<" "<<a[2]<<endl;

                if(a[1]==0 && a[2]==0) {impo=1;break;}
                else if(a[1]>a[2]) {a[1]--;s+="B";}
                else if(a[1]<=a[2]) {a[2]--;s+="Y";}

            }
           else if (s[s.length()-1]=='B') {
                if(a[0]==0 && a[2]==0) {impo=1;break;}
                else if(a[0]>a[2]) {a[0]--;s+="R";}
                else if(a[0]<=a[2]) {a[2]--;s+="Y";}
                
            }
            else if (s[s.length()-1]=='Y') {
                if(a[1]==0 && a[0]==0) {impo=1;break;}
                else if(a[1]>a[0]) {a[1]--;s+="B";}
                else if(a[1]<=a[0]) {a[0]--;s+="R";}
//                cout<<s<<"  * "<<a[0]<<" "<<a[1]<<endl;

            }
 
        }
        //cout<<s<<"..."<<endl;
        printf("Case #%d: ",kk);

        if(impo==1 || s[0]==s[s.length()-1]) printf("IMPOSSIBLE\n");
        else cout<<s<<endl;

    }
    
    
    return 0;
}

