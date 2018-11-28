#include <iostream>
#include <string>
using namespace std;

int main()
{
    string n;
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        cin>>n;
        int flag=0, index=-1;
        for(long long i=n.length()-1; i>=0; i--){
            if(i==0){
                if(n[i]==n[i+1]&&flag){
                    index = i;
                }
                continue;
            }
            int d1 = n[i] - '0';
            int d2 = n[i-1] - '0';
            if(d1 < d2 || (d1==d2&&flag==1)){
                index = i;
                flag=1;
            }else{
                flag=0;
            }
        }
        
        if(index>0){
            n[index-1] = n[index-1] - 1;
            for(int i=index; i<n.length(); i++){
                n[i] = '9';
            }
        }else if(index==0){
            n[index] = n[index] - 1;
            for(int i=index+1; i<n.length(); i++){
                n[i] = '9';
            }
                
        }
        if(n[0]=='0'){
            n = n.substr(1);
        }
        cout<<"Case #"<<tc<<": "<<n<<endl;
    }
    return 0;
}
