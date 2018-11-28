#include <cstdio>
#include <string>
using namespace std;
string out;
int n;
void solve(int r,int y,int b,char c = '\0'){
    if(r < 0 || y < 0 || b < 0)
        return;
    if(r + y + b == 0 && out.back() != out.front()){
        printf("%s\n",out.c_str());
        throw 0;
    }
    if(c == '\0'){
        out.push_back('R');
        solve(r-1,y,b,'R');
        out.pop_back();
        out.push_back('Y');
        solve(r,y-1,b,'Y');
        out.pop_back();
        out.push_back('B');
        solve(r,y,b-1,'B');
        out.pop_back();
    }else{
        if(c == 'R'){
            if(y > b){
                out.push_back('Y');
                solve(r,y-1,b,'Y');
                out.pop_back();
            }else{
                out.push_back('B');
                solve(r,y,b-1,'B');
                out.pop_back();
            }
        }else if(c == 'Y'){
            if(r > b){
                out.push_back('R');
                solve(r-1,y,b,'R');
                out.pop_back();
            }else{
                out.push_back('B');
                solve(r,y,b-1,'B');
                out.pop_back();
            }
        }else{
            if(r > y){
                out.push_back('R');
                solve(r-1,y,b,'R');
                out.pop_back();
            }else{
                out.push_back('Y');
                solve(r,y-1,b,'Y');
                out.pop_back();
            }
        }
    }
}
int main(){
    freopen("B-small-attempt5.in","r",stdin);
    freopen("B-small-attempt5.out","w",stdout);
    int t;
    scanf("%d",&t);
    int r,o,y,g,b,v;
    for(int tc = 1; tc <= t; tc++){
        out.clear();
        scanf("%d",&n);
        scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
        try{
            printf("Case #%d: ",tc);
            solve(r,y,b);
            printf("IMPOSSIBLE\n");
        }catch(int c){
            ;
        }
    }
    return 0;
}
