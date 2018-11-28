#include <iostream>
#include <math.h>
#include <set>
using namespace std;

class Cake{
public:
    double radius;
    double height;

    double getTop() const{
        return radius * radius;
    }
    double getSide() const{
        return 2.0 * radius * height;
    }
    double getTotal() const{
        return getTop() + getSide();
    }

};

struct HeightCompare{
    bool operator()(const Cake* a, const Cake* b){
        return a->getSide() > b->getSide();
    }
};


Cake* c[1000];
multiset<Cake*, HeightCompare> cakeSet;
double result(int n, int k){
    std::sort(c, c + n,
          [](const Cake* a, const Cake* b) -> bool
          { return a->radius > b->radius; } );
    
    double max = 0;
    double total = 0;
    int count = 0;
    for (int j=0; j<n; j++){
        total = 0;
        count = 0;
        cakeSet.clear();
        for (int y=j+1; y<n; y++){
            cakeSet.insert(c[y]);
        }
        for (auto c : cakeSet){
            if (k - 1 == 0) break;
            //cout << c->radius << endl;
            total += c->getSide();
            if (++count == k - 1)
                break;
        }
        total += c[j]->getTotal();
        if (total > max)
            max = total;
    }
    
    return max * M_PI;
}



int main(){
    int t, n, k, r, h;
    cin >> t;
    for (int i=1; i<=t; ++i){
        cin >> n >> k;
        for (int j=0; j<n; j++){
            cin >> r >> h;
            c[j] = new Cake();
            c[j]->radius = r;
            c[j]->height = h;

        }
        printf("Case #%i: %.9lf\n", i, result(n, k));
    }
    return 0;
}