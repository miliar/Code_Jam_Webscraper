#include<bits/stdc++.h>
using namespace std;
int r,c;
string func(string str,int ind){
    char curr=str[ind];
    for (int i=ind-1; i>=0; i--){
        if(str[i]=='?')str[i]=curr;
        else {curr=str[i];}
    }
    curr=str[ind];
    for (int i=ind+1; i<c; i++){
        if(str[i]=='?')str[i]=curr;
        else {curr=str[i];}
    }
    return str;
}

int comp(string s1, string s2){
    for (int i=0; i<c; i++){
        if(s1[i]!='?' && s2[i]!='?')return 0;
        
    }
    return 1;
}

int main(){
    int t;
    cin>>t;
    for (int i=0; i<t; i++){
        
        cin>>r>>c;
        int flag=0;
        string str[r];
        int start=-1,ind=-1;
        for (int j=0; j<r; j++){
            cin>>str[j];
            for (int h=0; h<c && flag==0; h++){
                if (str[j][h]!='?'){
                    start=j;
                    //cout<<str[j];
                    ind=h;
                    flag=1;
                    break;
                    
                }
            }
        }
        str[start]=func(str[start],ind);
        //cout<<str[start];
        int temp=start;
        for (int k=start-1; k>=0; k--){
            if (comp(str[temp],str[k])==1){
                str[k]=str[temp];
            }
            else{
                for (int h=0; h<c; h++){
                    if (str[k][h]!='?'){
                        str[k]=func(str[k],h);
                        temp=k;
                        break;
                    }
                }
            }
        }
        temp=start;
        for (int k=start+1; k<r; k++){
            if (comp(str[temp],str[k])==1){
                //if (k==r-1)cout<<str[temp];
                str[k]=str[temp];
            }
            else{
                for (int h=0; h<c; h++){
                    if (str[k][h]!='?'){
                        str[k]=func(str[k],h);
                        //cout<<h;
                        temp=k;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<i+1<<":"<<endl;
        for (int i=0; i<r; i++){
            cout<<str[i]<<endl;
        }
    
        
    }
    
    return 0;
}
