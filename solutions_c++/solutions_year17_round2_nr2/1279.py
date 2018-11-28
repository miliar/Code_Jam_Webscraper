#include <fstream>

using namespace std;

int main() {
    ifstream infile("B-small-attempt0.in");
    ofstream outfile("B-small-attempt0.out");

    int T;
    infile>>T;

    for(int t=1;t<=T;++t){
        int n, r, o, y, g, b, v;
        infile>>n>>r>>o>>y>>g>>b>>v;

        if(r+y<b || r+b<y || b+y<r){
            outfile<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            int x = max(max(r, y), b);
            if(x==r){
                string s(x,'R');
                int j = 0;
                for(int i=0;i<y;++i){
                    for(;j<s.size();++j){
                        if(s[j]=='R'){
                            s.insert(s.begin()+j+1, 'Y');
                            ++j;
                            break;
                        }
                    }
                }
                for(int i=0;i<b;++i){
                    for(;j<s.size();++j,j%=s.size()){
                        if(s[j]=='R'){
                            s.insert(s.begin()+j+1, 'B');
                            ++j;
                            break;
                        }
                    }
                }
                outfile<<"Case #"<<t<<": "<<s<<endl;
            }
            else if(x==y){
                string s(x,'Y');
                int j = 0;
                for(int i=0;i<r;++i){
                    for(;j<s.size();++j){
                        if(s[j]=='Y'){
                            s.insert(s.begin()+j+1, 'R');
                            ++j;
                            break;
                        }
                    }
                }
                for(int i=0;i<b;++i){
                    for(;j<s.size();++j,j%=s.size()){
                        if(s[j]=='Y'){
                            s.insert(s.begin()+j+1, 'B');
                            ++j;
                            break;
                        }
                    }
                }
                outfile<<"Case #"<<t<<": "<<s<<endl;
            }
            else{
                string s(x,'B');
                int j = 0;
                for(int i=0;i<y;++i){
                    for(;j<s.size();++j){
                        if(s[j]=='B'){
                            s.insert(s.begin()+j+1, 'Y');
                            ++j;
                            break;
                        }
                    }
                }
                for(int i=0;i<r;++i){
                    for(;j<s.size();++j,j%=s.size()){
                        if (s[j] == 'B') {
                            s.insert(s.begin() + j + 1, 'R');
                            ++j;
                            break;
                        }
                    }
                }
                outfile<<"Case #"<<t<<": "<<s<<endl;
            }
        }
    }

    infile.close();
    outfile.close();
    return 0;
}