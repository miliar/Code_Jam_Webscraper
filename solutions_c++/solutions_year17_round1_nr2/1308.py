#include <iostream>
#include <math.h>
using namespace std;


bool calc(int **q, int *ingredients, int cur_ingredient, int multiply, int n, int p) {
    if(cur_ingredient == n)
        return true;
    bool flag = false;
    for(int i=0;i<p;i++) {
        int ni=multiply*ingredients[cur_ingredient];
        if(!(q[cur_ingredient][i]<=float(ni)*1.1 && q[cur_ingredient][i]>=float(ni)*0.9))
            continue;
        bool next = calc(q, ingredients, cur_ingredient + 1, multiply, n, p);
        if(next) {
            flag = true;
            break;
        }
    }
    return flag;
}


void _main(int tc) {
    int n, p;
    cin>>n>>p;
    int *ingredients = new int[n];
    for(int i=0;i<n;i++)
        cin>>ingredients[i];
    int **q = new int*[n];
    for(int i=0;i<n;i++) {
        q[i] = new int[p];
        for(int j=0;j<p;j++)
            cin>>q[i][j];
    }
    int res=0;
    for(int i=0;i<p;i++) {
        double left = float(q[0][i])/(1.1*float(ingredients[0]));
        double right = float(q[0][i])/(0.9*float(ingredients[0]));
        int first = int(ceil(left));
        bool flag1 = false;
        for(int nn = first; nn<=right;nn++) {
            bool cur = calc(q, ingredients, 1, nn, n, p);
            if(cur) {
                flag1 = true;
                break;
            }
        }
        if(flag1) res++;
    }
    cout<<"Case #"<<tc<<": "<<res<<endl;
}

int main(int argc, char* argv[])
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++) {
        _main(i+1);
    }

    return 0;
}
