#include <bits/stdc++.h>

using namespace std;

int main () {
    int tt; 
    cin >> tt;
    for (int cases = 1; cases <= tt; ++cases) {
        cout << "Case #" << cases << ": ";
        int n;
        cin >> n; 
        int r, o, y, g, b, v;
        cin >> r >> o >> y >> g >> b >> v;
        string sb = "", sr = "", sy = "";
        
        if (o > 0 && o > b - 1) {
            if (o == b && r + y + g + v == 0) {
                for (int i = 0; i < o; ++i)
                    cout << "OB";
                cout << "\n";
                continue;
            }
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for (int i = 0; i < o; ++i) {
            if (sb == "")
                sb = "B";
            sb += "OB";
            --o; 
            --b;
            n -= 2;
        }
        
        if (v > 0 && v > y - 1) {
            if (v == y && r + b + g + o == 0) {
                for (int i = 0; i < v; ++i)
                    cout << "YV";
                cout << "\n";
                continue;
            }
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for (int i = 0; i < v; ++i) {
            if (sy == "")
                sy = "Y";
            sy += "VY";
            --v; 
            --y;
            n -= 2;
        }
        
        if (g > 0 && g > r - 1) {
            if (g == r && o + y + b + v == 0) {
                for (int i = 0; i < g; ++i)
                    cout << "GR";
                cout << "\n";
                continue;
            }
            cout << "IMPOSSIBLE\n";
            continue;
        }
        for (int i = 0; i < g; ++i) {
            if (sr == "")
                sr = "R";
            sr += "GR";
            --g; 
            --r;
            n -= 2;
        }

        if (r > 1 || b > 1 || y > 1) {
            if (b >= r && b >= y) {
                if (b > r + y) {
                    cout << "IMPOSSIBLE\n";
                    continue;
                }
                while (b > 1 && r != y) {
                    if (r > y) {
                        if (sb == "") {
                            sb = "B";
                        }
                        sb += "RB";
                        --b;
                        --r;
                        n -= 2;
                    }
                    else if (r < y) {
                        if (sb == "") {
                            sb = "B";
                        }
                        sb += "YB";
                        --b;
                        --y;
                        n -= 2;
                    }
                }

                while (b > 1 && b > r) {
                    if (b == 2) {
                        if (r > y) {
                            if (sb == "") {
                                sb = "B";
                            }
                            sb += "RB";
                            --b;
                            --r;
                            n -= 2;
                        } else {
                            if (sb == "") {
                                sb = "B";
                            }
                            sb += "YB";
                            --b;
                            --y;
                            n -= 2;

                        }
                        break;
                    }
                    if (sb == "") {
                        sb = "B";
                    }
                    sb += "RBYB";
                    --r;
                    --y;
                    b -= 2;
                    n -= 4;
                }
            }
            else if (r >= b && r >= y) {
                if (r > b + y) {
                    cout << "IMPOSSIBLE\n";
                    continue;
                }
                while (r > 1 && b != y) {
                    if (b > y) {
                        if (sr == "") {
                            sr = "R";
                        }
                        sr += "BR";
                        --b;
                        --r;
                        n -= 2;
                    }
                    else if (b < y) {
                        if (sr == "") {
                            sr = "R";
                        }
                        sr += "YR";
                        --r;
                        --y;
                        n -= 2;
                    }
                }

                while (r > 1 && r > b) {
                    if (r == 2) {
                        if (b > y) {
                            if (sr == "") {
                                sr = "R";
                            }
                            sr += "BR";
                            --b;
                            --r;
                            n -= 2;
                        }
                        else {
                            if (sr == "") {
                                sr = "R";
                            }
                            sr += "YR";
                            --r;
                            --y;
                            n -= 2;
                        }
                        break;
                    }
                    if (sr == "") {
                        sr = "R";
                    }
                    sr += "BRYR";
                    --y;
                    --b;
                    r -= 2;
                    n -= 4;
                }
            }
            else if (y >= b && y >= r) {
                if (y > b + r) {
                    cout << "IMPOSSIBLE\n";
                    continue;
                }
                while (y > 1 && b != r) {
                    if (b > r) {
                        if (sy == "") {
                            sy = "Y";
                        }
                        sy += "BY";
                        --b;
                        --y;
                        n -= 2;
                    }
                    else if (b < r) {
                        if (sy == "") {
                            sy = "Y";
                        }
                        sy += "RY";
                        --r;
                        --y;
                        n -= 2;
                    }
                }
                
                while (y > 1 && y > b) {
                    if (y == 2) {
                        if (b > r) {
                            if (sy == "") {
                                sy = "Y";
                            }
                            sy += "BY";
                            --b;
                            --y;
                            n -= 2;
                        }
                        else {
                            if (sy == "") {
                                sy = "Y";
                            }
                            sy += "RY";
                            --r;
                            --y;
                            n -= 2;
                        }
                        break;
                    }
                    if (sy == "") {
                        sy = "Y";
                    }
                    sy += "BYRY";
                    --r;
                    --b;
                    y -= 2;
                    n -= 4;
                }
            }
        }
        while (r + b + y > 0) {
            if (r > 0) {
                if (sr != "") {
                    cout << sr;
                    sr = "";
                } else 
                    cout << "R";
                --r;
            }
            if (b > 0) {
                if (sb != "") {
                    cout << sb;
                    sb = "";
                } else
                    cout << "B";
                --b;
            }
            if (y > 0) {
                if (sy != "") {
                    cout << sy;
                    sy = "";
                } else
                    cout << "Y";
                --y;
            }
        }
        cout << "\n";
    }
}
