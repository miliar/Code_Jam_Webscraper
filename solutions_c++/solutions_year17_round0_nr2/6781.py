#include <bits/stdc++.h>
using namespace std;

int main(){
    int h;
    cin>>h;
    for(int t=0;t<h;t++){
        int flag=0;
        string v;
        cin>>v;
        if(v.length()==1){
	        cout<<"Case #"<<t+1<<": ";
	        cout<<v;
	        if(t+1 < h){
	            cout<<endl;
	        }
	        flag=2;
	    }
	    else{
	        while(1){
	        for(int j=0;j<v.length()-1;j++){
	            if(j==0 && (v[0]>v[1])){
	                v[0]=v[0]-1;
	                for(int k=1;k<v.length();k++){
	                    v[k]='9';
	                }
	            }
	            else{
	                if(v[j] > v[j+1]){
	                    if(v[j]==0){
	                        v[j]='9';
	                    }
	                    else{
	                        v[j]=v[j]-1;
	                    }
	                    for(int k=j+1;k<v.length();k++){
	                        v[k]='9';
	                    }
	                }
	            }
        	}
	        for(int k=0;k<v.length()-1;k++){
	            if(v[k]>v[k+1]){
	                flag=1;
	                break;
	            }
	        }
	        if(flag==0){
	            break;
	        }
	        flag=0;
	        }
	    }
	    if(flag!=2){
	        cout<<"Case #"<<t+1<<": ";
	        for(int k=0;k<v.length();k++){
	            //cout<<"hlo"<<endl;
	            if(k==0){
	                if(v[0]!='0'){ //cout<<"haha"<<endl;
	                    cout<<v[k];
	                }
	            }
	            else{
	                cout<<v[k];
	            }
	        }
	        if(t+1!=h){
                cout<<endl;
	        }
	    }
    }
	return 0;
}
