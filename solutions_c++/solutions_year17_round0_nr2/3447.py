#include <iostream>
#include <cstdio>
using namespace std;

struct OPF{

    OPF(){
        int N;
        cin >> N;
        for(int t=0; t<N; ++t){
            string s;      int k;
            cin >> s >> k;
            int r=0;
            for(int i=0; i<=s.size()-k; ++i){
                if(s[i]=='-'){
                    for(int j=0; j<k; ++j) s[i+j]='+'+'-'-s[i+j];
                    r++;
                }
            }
            for(int i=s.size()-k+1; i<s.size(); ++i){
                if(s[i]=='-'){
                    r=-1;
                    break;
                }
            }
            cout << "Case #" << t+1 << ": " << (r>=0?to_string(r):"IMPOSSIBLE") << endl;
        }
    }
};

struct TIN{
    TIN(){
        int T;
        cin >> T;
        for(int t=0; t<T; ++t){
            string s;
            cin >> s;
            for(int i=s.size()-1; i>0; --i){
                if(s[i-1]>s[i]){
                    for(int j=i; j<s.size(); ++j){
                        s[j]='9';
                    }
                    for(int r=1, j=i-1; r; --j){
                        if(s[j]=='0'){
                            s[j]='9';
                        }else{
                            s[j]--;
                            r=0;
                        }
                    }

                }
            }
            if(s[0]=='0') s=s.substr(1, s.size()-1);
            cout << "Case #" << t+1 << ": " << s << endl;
        }
    }
};

int main(int argc, char *argv[])
{
//    freopen ("test.in","r",stdin);
    TIN();
    return 0;
}
