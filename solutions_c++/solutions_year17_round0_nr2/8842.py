#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

inline bool Ordered(string a){
    const int lim=a.size();
    for(int i=1; i<lim; ++i){
        if(a[i-1]>a[i]){
            return false;
        }
    }
    return true;
}

int getInd(string a){
    int lim=a.size();
    bool isSort[lim];
    for(int i=0; i<lim; ++i){
        isSort[i]=0;
    }
    isSort[0]=1;
    for(int i=1; i<lim; ++i){
        if(a[i-1]<=a[i]){
            isSort[i]=1;
        }else{
            break;
        }
    }
    for(int i=1; i<lim; ++i){
        if(!isSort[i]){
            return i-1;
        }
    }
}

int countDups(string a, int beg){
    for(int i=0; i<=beg; i++){
        if(a[i]==a[beg]){
            return i;
        }
    }
    return beg;
}


string order(string a){
    if(a.size()==1){
        return a;
    }
    else if(Ordered(a)){
        return a;
    }else{
        string rstring=a;
        int pos=getInd(a);
        if(pos==0){
            char a1=('0'==rstring.at(0))? '9': rstring.at(pos)-1;
            rstring[0]=a1;
            for(int i=pos+1; i<a.size(); ++i){
                rstring[i]='9';
            }
        }else{
            pos=countDups(a, pos);
            if(a[pos]=='1'){
                rstring[0]='0';
                for(int i=pos+1; i<a.size(); ++i){
                    rstring[i]='9';
                }
            }else{            
                char a1=('0'==rstring.at(pos))? '9': rstring.at(pos)-1;
                rstring[pos]=a1;
                for(int i=pos+1; i<a.size(); ++i){
                    rstring[i]='9';
                }
            }
        }
        return rstring; 
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    int tc;
    cin>>tc;
    for(int i=1; i<=tc; ++i){
        string n;
        cin>>n;
        cout<<"Case #"<<i<<": ";
        n=order(n);
        for(int i=0; i<n.size();++i){
            if(n[i]!='0'){
                cout<<n[i];
            }
        }
        cout<<endl;
    }
    return 0;
}
