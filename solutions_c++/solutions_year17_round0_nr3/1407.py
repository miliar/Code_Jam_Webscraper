#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;


int main()
{
    string file_name = "C-large";
    ifstream f1((file_name+".in").c_str());
    ofstream f2((file_name+".out").c_str());
    int T;
    f1 >> T;
    for(int t = 0; t < T; ++t)
    {
        f2 << "Case #" << t+1 << ": ";
        unsigned long long int n, k;
        f1 >> n >> k;
        set<unsigned long long int> used;
        map<unsigned long long int, unsigned long long int> count;
        used.insert(n);
        count[n]++;
        set<unsigned long long int>::iterator it;
        while(true)
        {
            unsigned long long int head;
            it = used.end();
            --it;
            head = *it;
            if(k > count[head])
            {
                k -= count[head];
                count[head/2] += count[head];
                count[(head-1)/2] += count[head];
                used.insert(head/2);
                used.insert((head-1)/2);
                count[head] = 0;
                used.erase(head);
            }else
            {
                f2 << head/2 << ' ' << (head-1)/2 << endl;
                break;
            }
        }
    }
    return 0;
}

