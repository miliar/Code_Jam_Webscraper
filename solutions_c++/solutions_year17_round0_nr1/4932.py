#include <iostream>
#include <string>  
#include <stdio.h>
using namespace std;

int main() {
	// your code goes here
    string test;
    //cin>>test;
    getline(cin, test);
    int tost = stoi(test);
    int arr[2000];
    int mile[2000];
    int ind =0;
    //cout<<test<<endl;
    for(int t= 1;t<=tost;t++){
        string st;
        if(!getline(cin, st))
            break;
            
        //cout<<st<<endl;
        ind = 0;
        while((st.at(ind) - ' ') !=0){
            //cout<<crr[ind]<<endl;
            if(st.at(ind) == '+')
                arr[ind] = 1;
            else
                arr[ind] = 0;
            mile[ind] = 0;
            ind++;
        }
        //cout<<ind<<endl;
        int r_s = ind+1;
        int nrr[5];
        int nind = 0;
        while(r_s<st.length()){
            //cout<<st.at(r_s)<<endl;
            nrr[nind] = st.at(r_s) - '0';
            r_s++;
            nind++;
            
        }
        int mul = 1;
        int num = 0;
        for(int i=nind-1;i>=0;i--){
            num += mul* nrr[i];
            mul *=10;
        }
        int chk = 0;
        int ans = 0;
        int range = 0;
        //cout<<ind<<"-->"<<endl;
        
        for(int i=0;i<ind;i++){
            if(arr[i] == chk){
                
                range = (i+num)-1;
            
                //cout<<range<<" "<<ind<<endl;
                if(range>=ind){
                    ans = -1;
                    break;
                }
                mile[range] = -1;
                ans++;
                if(chk == 0)
                    chk = 1;
                else
                    chk = 0;
            }
            if(mile[i]==-1){
                if(chk == 0)
                    chk = 1;
                else
                    chk = 0;
            }
                
            
        }
        cout<<"Case #"<<t<<": ";
        if(ans==-1){
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            cout<<ans<<endl;
        }
        //cout<<num<<endl;
        
    }
	return 0;
}
