#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <stdlib.h>
#include <cmath>
#include <math.h>
#include <fstream>
#include <bitset>
using namespace std;
long long n, t, k;
int main(){
    ifstream in;
    in.open("1.txt");
    ofstream out;
    out.open("2.txt");
    in >> t;
    for (int i=0;i<t;i++){
        in >> n >> k;
        out << "Case #" << i + 1 << ": ";
        long long number = 1;
        long long f = 1;
        long long s = 0;
        long long pl = 1;
        long long m = -1;
        if (k == n){
            out << 0 << " " << 0 << endl;
            continue;
        }
        while (true){
            if (k <= pl){
                if (number == 1){
                    out << n / 2 << " " << n - n / 2 - 1 << endl;
                }
                else{
                    if (k <= f){
                        out << n / 2 << " " << n - n / 2 - 1 << endl;
                    }
                    else{
                        out << m / 2 << " " << m - m / 2 - 1 << endl;
                    }
                }
                break;
            }
            else{
                k -= pl;
                pl *= 2;
                long long c, d, f1, s1;
                f1 = 0;
                s1 = 0;
                if (n % 2 == 0) number = 2;
                if (number != 2){
                    f *= 2;
                    n /= 2;
                }
                else{
                    if (n % 2 == 0){
                        c = n / 2;
                        d = n / 2 - 1;
                        f1 += f;
                        s1 += f;
                        if (m != -1){
                            s1 += 2 * s;
                        }
                    }
                    else{
                        c = n / 2;
                        d = n / 2 - 1;
                        f1 += 2 * f;
                        if (m != -1){
                            f1 += s;
                            s1 += s;
                        }
                    }
                    n = c;
                    m = d;
                    f = f1;
                    s = s1;
                }
            }
        }
    }
    out.close();
    return 0;
}
