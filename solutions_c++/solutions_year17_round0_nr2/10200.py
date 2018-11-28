#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;

void getTidy(string s, int t){
    for(int i=0;i<s.size()-1;i++){
        int j=i+1;
        if(s[j]<s[i]){
            int pos = i;
            while(pos>=0 && s[pos--]==s[i]);
            pos++;
            if(s[pos]!=s[i])
                pos++;
            s[pos] = s[pos] - 1;
/*          if(s[i]=='1'){
                s[pos]='0';
                pos++;
            }
            for(int m=pos;m<=i;m++){
                if(s[i]=='1')
                    s[m]='9';
                else
                    s[m]=s[m] - 1;
            }
            */
            for(int k=pos+1;k<s.size();k++)
                s[k]='9';
            break;
        }
    }
    cout<<"Case #"<<t<<": "<<atoll(s.c_str())<<endl;
    // remove the leading zeros if any
}

int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        string s;
        cin>>s;
        getTidy(s,i+1);
    }
    return 0;
}
