#include <iostream>
#include <limits.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
int main() {

    freopen("cjinput.txt", "r", stdin);
    freopen("cjoutput.txt", "w", stdout);

    int t;
    cin>>t;
    string s;
    int n;
    ull num;

    for(int j=1;j<=t;j++) {
        cin>>num;
        if(num%10)
            s=to_string(num);
        else 
            s=to_string(num-1);

        n=s.length();
        int i,k;
        for(i=0;i<n-1;i++) {
            if(s[i]<=s[i+1])
                continue;
            else 
                break;
        }

        k=i;

        if(k<n-1) {

            while(k>0&&s[k]==s[k-1]) 
                k--;

            // if(k<=0) {
            //     k=0;
            // }

            s[k]=s[k]-1;

            k++;

            while(k<n) {
                s[k++]='9';
            }

        }

        cout << "Case #" << j << ": " ;
        for(int i=0;i<n;i++) {
            if(s[i]!='0') {
                cout<<s[i];
            }
        }
        cout<<endl;





    }

    

}