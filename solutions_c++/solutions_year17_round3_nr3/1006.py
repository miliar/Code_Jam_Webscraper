#include <bits/stdc++.h>
using namespace std;
double f, a[100], p;


int main(){
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output_c.txt", "w", stdout);
    int T, n, k;

    cin >> T;
    for(int t=1; t<=T; t++){
        p = 1;
        cin >> n >> k >> f;
        for(int i=0; i<n; i++)
            cin >> a[i];
        sort(a, a+n);

        int num = 1;
        while(1){
            if(num==n){
                double tm = f/num;
                for(int i=0;i<num;i++){
                    a[i] += tm;
                }
                break;
            }

            while(a[num] == a[num-1] && num<n){
                num++;
            }
            double gap = a[num] - a[num-1];
            double tmp = f/num;


            if(num == n){
                for(int i=0;i<num;i++){
                    a[i] += tmp;
                }
                break;
            }
            if(num * gap - f > 1e-9){
                for(int i=0;i<num;i++){
                    a[i] += tmp;
                }
                break;
            }
            else{
                for(int i=0;i<num;i++){
                    a[i] = a[num];
                }
                f -= num * gap;
                num++;
            }
        }


        for(int i=0; i<n; i++)
            p*=a[i];

        cout.precision(6);
        cout << "Case #" << t << ": " <<fixed<< p<< "\n";
    }
    return 0;
}
