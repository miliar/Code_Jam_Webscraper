#include <iostream>
#include <list>

#define tab "\t"
#define min(x,y) (x > y ? y : x)
#define max(x,y) (x > y ? x : y)

using namespace std;


int main() {
    
    int t;
    unsigned long long int N, k, first, last, place, ls, rs, x1f, x1l, x1z, x2f, x2l, x2z;
    list<unsigned long long int> sf, sl, sz;
    list<unsigned long long int>::iterator iter, inp, itz, itf, itl;
    bool order;
    char s[2000];
    
    cin >> t;
    
    for (int i = 0; i < 2000; i++)
        s[i] = '.';
    
    for (int ci = 1; ci <= t; ++ci) {
        
        cin >> N >> k;
        
        if (k == N) {
            cout << "Case #" << ci << ": " << 0 << " " << 0 << endl;
            continue;
        }
        
        sf.clear();
        sl.clear();
        sz.clear();
        sf.push_front(1);
        sl.push_front(N);
        sz.push_front(N);
        
        for(int p = 1; p <= k; p++) {
            
/*            cout << "person " << p << endl;

            for (unsigned long long int i : sf) {
                std::cout << i << tab;
            }
            cout << endl;
            for (unsigned long long int i : sl) {
                std::cout << i << tab;
            }
            cout << endl;
            for (unsigned long long int i : sz) {
                std::cout << i << tab;
            }
            cout << endl;
*/
            first = sf.front();
            last  = sl.front();
            sf.pop_front();
            sl.pop_front();
            sz.pop_front();
            
            place = first + (last - first) / 2;
            order = ((last - first) % 2 == 1); // equal segments
            
            bool no_first = place == first;
            bool no_last = place == last;
            
            ls = place - first;
            rs = last - place;

            x1f = first;
            x1l = place - 1;
            x1z = place - first;
            
            x2f = place + 1;
            x2l = last;
            x2z = last - place;
            
            bool x1first = x1z > x2z ? 1 : (x1z == x2z && x1f < x2f);
            
            if (sz.empty()) {
                if (x1first) {
                    if (!no_first) {
                        sf.push_front(x1f);
                        sl.push_front(x1l);
                        sz.push_front(x1z);
                    }
                    if (!no_last) {
                        sf.push_back(x2f);
                        sl.push_back(x2l);
                        sz.push_back(x2z);
                    }
                } else {
                    if (!no_last) {
                        sf.push_front(x2f);
                        sl.push_front(x2l);
                        sz.push_front(x2z);
                    }
                    if (!no_first) {
                        sf.push_back(x1f);
                        sl.push_back(x1l);
                        sz.push_back(x1z);
                    }
                }
            } else {
                for (itf = sf.begin(), itl = sl.begin(), itz = sz.begin();
                     itf != sf.end(), itl != sl.end(), itz != sz.end();
                     ++itf, ++itl, ++itz){
                    if (x1z > *itz || (x1z == *itz && x1f < *itf))
                        break;
                }
                
                sf.insert(itf, x1f);
                sl.insert(itl, x1l);
                sz.insert(itz, x1z);
                
                for (itf = sf.begin(), itl = sl.begin(), itz = sz.begin();
                     itf != sf.end(), itl != sl.end(), itz != sz.end();
                     ++itf, ++itl, ++itz){
                    if (x2z > *itz || (x2z == *itz && x2f < *itf))
                        break;
                }
                
                sf.insert(itf, x2f);
                sl.insert(itl, x2l);
                sz.insert(itz, x2z);
                
            }
            
/*            if (!order) {
                // push left segment first
                if (!no_first) {
                    sf.push_back(first);
                    sl.push_back(place - 1);
                }
                if (!no_last) {
                    sf.push_back(place + 1);
                    sl.push_back(last);
                }
            } else {
                // push right segment first
                if (!no_last) {
                    sf.push_back(place + 1);
                    sl.push_back(last);
                }
                if (!no_first) {
                    sf.push_back(first);
                    sl.push_back(place - 1);
                }
            }
*/
 //           cout << place << tab << order << endl;
//            s[place] = 'o';
            
//            for (int i = 1; i <= N; i++)
//                cout << s[i];

//            cout << endl;
//            cin.get();
        }
        
        cout << "Case #" << ci << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
    }
}