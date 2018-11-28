#include<bits/stdc++.h>
#include<fstream>
using namespace std;

int main(){
    int t;
    ifstream f ;
    f.open("A-large.in");
    ofstream out ;
    out.open("out.txt");
    f >> t;
    //scanf("%d",&t);
    int a=1;
    while(a<=t){
        string s;
        f >> s;
        int k;
        f >> k;
        //getchar();
        //cin >> s;
        //scanf("%d",&k);
        int i,n,ans=0;
        n = s.size();
        for(i=0;i<=n-k; i++){
            if(s[i]=='-'){
                ans++;
                int ct = 0;
                while(ct<k){
                    if(s[i+ct]=='-'){
                        s[i+ct]='+';
                    }
                    else{
                        s[i+ct]='-';
                    }
                    ct++;
                }
              //  cout << s << endl;
            }
        }
        int flag=0;
        out << "Case #" << a << ": ";
        for(i=0;i<n;i++){
            if(s[i]=='-'){
                out << "IMPOSSIBLE" << endl;
                flag=1;
                break;
            }
        }
        if(flag==0){
            out << ans << endl;
        }
        a++;
    }
    f.close();
    out.close();
}
