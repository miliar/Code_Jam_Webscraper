#include <bits/stdc++.h>

using namespace std;

int main(){
    int T;
    scanf("%d", &T);
    for ( int t = 1; t <= T; t++){
        char in[1010];
        bool ok = true;
        int w, total=0;
        priority_queue<int, vector<int>, std::greater<int> > q;
        scanf("%s %d", in, &w);
        int dl = strlen(in);
        for(int i=0;i<dl;i++){
            if(q.size()>0){
                if(q.top()==i)q.pop();
            }
            char c = (q.size()%2==1?'+':'-');
            if(in[i]==c){
                if(i>dl-w){
                    ok = false;
                    break;
                }
                q.push(i+w);
                total++;
            }
        }
        
        printf("Case #%d: ", t);
        if(ok){
            printf("%d\n", total);
        }else{
            printf("IMPOSSIBLE\n");
        }
        
    }


    return 0;
}