#include <fstream>
#include <list>
//#include <set>
#define INF 99999999

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

struct elem{long long Ls; long long Rs;};
struct elem2 {elem innerRange; long long middle; elem limits;} G;
long long steps;
bool solved;

list<elem2> intervals;
//set<elem2> intervals;
int T;

void new_interval(int, int);
void solve();


int main()
{
    cin >> T;
    long long n;
    for(int t = 1; t <= T; t++){
        cin >> n >> steps;
        new_interval(1, n);

        solved = false;
        solve();
        if(t == 50){
            t = 50;
        }
        cout << "Case #" << t << ": ";
        cout << G.innerRange.Rs <<" " << G.innerRange.Ls << '\n';
        intervals.clear();
    }
    return 0;
}

void solve(){
    if(solved) return;
    //pick best element
    list<elem2>::iterator it, pos;

    G.innerRange.Ls = -1;
    G.innerRange.Rs = -1;

    for(it = intervals.begin(); it != intervals.end(); ++it){
        elem2 el = *it;
        if(el.innerRange.Ls > G.innerRange.Ls){
            G = el;
            pos = it;
        }
        else if(el.innerRange.Ls == G.innerRange.Ls && el.innerRange.Rs > G.innerRange.Rs){
            G = el;
            pos = it;
        }
    }
    intervals.erase(pos);
    //intervals.remove(G);
    //get 2 new intervals
    new_interval(G.limits.Ls, G.middle - 1);
    new_interval(G.middle+1, G.limits.Rs);
    steps--;
    if(steps == 0){
        solved = true;
    }
    solve();
}



void new_interval(int a, int b){
    if(b >= a){
        elem2 main_elem;
        elem range;
        main_elem.middle = (a+b)/2;
        elem limits;
        limits.Ls = a;
        limits.Rs = b;
        range.Ls = main_elem.middle-a;
        range.Rs = b-main_elem.middle;
        main_elem.innerRange = range;
        main_elem.limits = limits;
        intervals.push_back(main_elem);
    }
}
