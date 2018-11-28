#include <iostream>

using namespace std;

int n, r, o, y, g, b, v;
int head, last;
bool first;

void pr()
{
    if(first) head = 1;
    first = false;
    cout << "R";
    n--;
    r--;
    last = 1;
}

void py()
{
    if(first) head = 2;
    first = false;
    cout << "Y";
    n--;
    y--;
    last = 2;
}

void pb()
{
    if(first) head = 3;
    first = false;
    cout << "B";
    n--;
    b--;
    last = 3;
}

int main()
{
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; ++tc){
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << tc << ": ";
        bool im = false;
        if(r < 2 * g) im = true;
        if(y < 2 * v) im = true;
        if(b < 2 * o) im = true;
        if(r > y + b) im = true; //tofix
        if(y > r + b) im = true; //tofix
        if(b > r + y) im = true; //tofix
        if(im){
            cout << "IMPOSSIBLE" << endl;
            continue; 
        }
        last = 0, head = 0;
        first = true;
        while(n){
            if(r == y && y == b){
                if(last == 0 && head == 0){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        py();
                        pb();
                    }
                    break;
                }
                if(last == 1 && head == 1){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pb();
                        pr();
                        py();
                    }
                    break;
                }
                if(last == 1 && head == 2){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pb();
                        py();
                        pr();
                    }
                    break;
                }
                if(last == 1 && head == 3){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pb();
                        py();
                        pr();
                    }
                    break;
                }
                if(last == 2 && head == 1){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        py();
                        pb();
                    }
                    break;
                }
                if(last == 2 && head == 2){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        py();
                        pb();
                    }
                    break;
                }
                if(last == 2 && head == 3){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        pb();
                        py();
                    }
                    break;
                }
                if(last == 3 && head == 1){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        py();
                        pb();
                    }
                    break;
                }
                if(last == 3 && head == 2){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        py();
                        pb();
                    }
                    break;
                }
                if(last == 3 && head == 3){
                    int now = n;
                    for(int i = 0; i < now / 3; ++i){
                        pr();
                        pb();
                        py();
                    }
                    break;
                }
            }
            if(r >= y && r >= b && last != 1){
                pr();
            } else if(y >= r && y >= b && last != 2){
                py();
            } else if(b >= r && b >= y && last != 3){
                pb();
            } else if(y >= b && last == 1){
                py();
            } else if(b >= y && last == 1){
                pb();
            } else if(r >= b && last == 2){
                pr();
            } else if(b >= r && last == 2){
                pb();
            } else if(r >= y && last == 3){
                pr();
            } else if(y >= r && last == 3){
                py();
            }
        }
        cout << endl;
    }
}
