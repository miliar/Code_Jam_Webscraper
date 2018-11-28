#include <bits/stdc++.h>
using namespace std;






int main() {
    freopen("inputB","r",stdin);
    freopen("outputB","w",stdout);
    int tests;
    cin>>tests;
    for (int T = 1; T <= tests; ++T) {
        int n, r, o, y, g, b, v;
        cin>>n>>r>>o>>y>>g>>b>>v;

        char arr[n+1];

        if(r>y+b||y>r+b||b>r+y) {cout<<"Case #"<<T<<": IMPOSSIBLE"<<endl;continue;}
        arr[0]='z';
        int num=0;
        int rt=r,yt=y,bt=b;
        while(r!=0||y!=0||b!=0){
            num++;


            if(rt>yt&&rt>bt){
                if(r>=y+b&&arr[num-1]!='R'){
                    arr[num]='R';
                    r--;
                    continue;
                }
                if(y>=r+b&&arr[num-1]!='Y'){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(b>=r+y&&arr[num-1]!='B'){
                    arr[num]='B';
                    b--;
                    continue;
                }

                if(arr[num-1]!='R'&&r!=0){

                    arr[num]='R';
                    r--;
                    continue;
                }
                if(arr[num-1]!='Y'&&y!=0){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(arr[num-1]!='B'&&b!=0){
                    arr[num]='B';
                    b--;
                    continue;
                }
            }
            if(yt>rt&&yt>bt){
                if(y>=r+b&&arr[num-1]!='Y'){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(r>=y+b&&arr[num-1]!='R'){
                    arr[num]='R';
                    r--;
                    continue;
                }
                if(b>=r+y&&arr[num-1]!='B'){
                    arr[num]='B';
                    b--;
                    continue;
                }

                if(arr[num-1]!='Y'&&y!=0){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(arr[num-1]!='R'&&r!=0){

                    arr[num]='R';
                    r--;
                    continue;
                }
                if(arr[num-1]!='B'&&b!=0){
                    arr[num]='B';
                    b--;
                    continue;
                }
            }
            if(bt>rt&&bt>yt){
                if(b>=r+y&&arr[num-1]!='B'){
                    arr[num]='B';
                    b--;
                    continue;
                }
                if(y>=r+b&&arr[num-1]!='Y'){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(r>=y+b&&arr[num-1]!='R'){
                    arr[num]='R';
                    r--;
                    continue;
                }


                if(arr[num-1]!='B'&&b!=0){
                    arr[num]='B';
                    b--;
                    continue;
                }
                if(arr[num-1]!='Y'&&y!=0){
                    arr[num]='Y';
                    y--;
                    continue;
                }
                if(arr[num-1]!='R'&&r!=0){

                    arr[num]='R';
                    r--;
                    continue;
                }

            }


            if(b>=r+y&&arr[num-1]!='B'){
                arr[num]='B';
                b--;
                continue;
            }
            if(y>=r+b&&arr[num-1]!='Y'){
                arr[num]='Y';
                y--;
                continue;
            }
            if(r>=y+b&&arr[num-1]!='R'){
                arr[num]='R';
                r--;
                continue;
            }
            if(arr[num-1]!='B'&&b!=0){
                arr[num]='B';
                b--;
                continue;
            }
            if(arr[num-1]!='Y'&&y!=0){
                arr[num]='Y';
                y--;
                continue;
            }
            if(arr[num-1]!='R'&&r!=0){

                arr[num]='R';
                r--;
                continue;
            }

        }


        cout<<"Case #"<<T<<": ";

        for (int i = 1; i <= n; ++i) {
            cout<<arr[i];
        }
        cout<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
