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

int main(int argc, char *argv[])
{
//    freopen ("test.in","r",stdin);
    OPF();
    return 0;
}
