#include <bits/stdc++.h>
using namespace std;


const int maxN = 55;

double a[maxN];


void work(){
    int n, k;
    double p;

    cin >> n >> k;
    cin >> p;
    for(int i = 0; i < n; i++)
        cin >> a[i];
    sort(a, a+n);
   

    double s = a[0];
    int j = -1;
    a[n] = 1.0;
    for(int i = 1; i < n+1; i++){
//        cout << a[i] << " " << s  << "  " << p << endl;
        double delta = i * a[i] - s;
        if(delta >= p-(1e-6)){
            j = i;
            break;
        }
        s += a[i];
    }

    double b = (s + p)/j; 
    double ret = 1.0;
    for(int i = 0; i <= n; i++)
        if(i < j)
            ret *= min(1.0, b);
        else
            ret *= min(1.0, a[i]);
    printf("%.7lf\n", ret);
}

int main(){

    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
