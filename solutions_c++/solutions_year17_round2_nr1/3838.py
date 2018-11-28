#include <bits/stdc++.h>
#define EPS 1e-12
using namespace std;

vector<pair<double,double>> ho;
double d ;
int n;
void reset(){
    ho.clear();
}
int main()
{
    freopen("C:\\Users\\Muhammed\\ClionProjects\\A-large.in","r",stdin);
    freopen("C:\\Users\\Muhammed\\ClionProjects\\A-large.out","w",stdout);
    int tests ;
    int counter = 1 ;
    cin >> tests;
    while(tests--){
        cin >> d >> n;
        reset();
        ho.resize(n);
        for(int i = 0 ; i < n ; i++){
            cin >> ho[i].first >> ho[i].second;
        }
        double mid = (d-ho[0].first)/ho[0].second;
        for(int i = 1 ; i < n ; i++){
            mid = max(mid,(d-ho[i].first)/ho[i].second);
        }

        printf("Case #%d: ",counter);
        printf("%.12lf\n",d/mid);
        counter++;
    }



    return 0;
}
