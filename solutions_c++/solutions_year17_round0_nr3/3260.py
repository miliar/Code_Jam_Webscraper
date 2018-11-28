#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stack>

using namespace std;

int main(void){
    int T;
//    char dump;
    FILE *fin=fopen("/Users/enyaning/Downloads/C-small-1-attempt0.in.txt","r");
//    FILE *fin=stdin;
    fscanf(fin,"%d",&T);
    for(int I=1;I<=T;I++){
        int n,k;
        fscanf(fin,"%d %d", &n,&k);
        
        int i=1;
        
        priority_queue<int> qu;
        qu.push(n);
        while(qu.size()){
            int x=qu.top()-1;
//            cout<<x+1<<endl;
            if(k==i++){
                printf("Case %d: %d %d\n",I,(x+1)/2,x/2);
                break;
            }
            qu.pop();
            if(x/2) qu.push(x/2);
            if((x+1)/2) qu.push((x+1)/2);
        }
    }
}

/*

3
---+-++- 3
+++++ 4
-+-+- 4
 
*/
