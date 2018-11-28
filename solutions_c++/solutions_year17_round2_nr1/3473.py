/* Code generated && tested by LizardCode for CodeFu */
#include <limits.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <list>
#include <queue>
#include <set>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;




int main()
{
    ifstream cin("input.txt");
   // ofstream cout("output.txt");
    
    FILE *fp;
    
    fp = fopen("file.txt","w");
    
    int t;
    int d,n;
    int pos,speed;
    
    cin >> t;
    
    int c = 1;
    double maxTime;
    while(t--) {
        vector< pair<int,int> > horse;
        cin >> d >> n;
        for(int i = 0; i < n; i++) {
            cin >> pos >> speed;
            horse.push_back(make_pair(pos,speed));
        }
        
        sort(horse.begin(), horse.end());
        
        maxTime = (d - horse[n-1].first) / (double)horse[n-1].second;;
        
        //cout << d-horse[n-1].first << endl;
        for(int i = n-2; i >= 0; i--) {
            double curTime = (d - horse[i].first) / (double)horse[i].second;
            if(curTime > maxTime) maxTime = curTime;
        }
        fprintf(fp, "Case #%d: %0.7f\n",c, d/maxTime);
//        cout << "Case #" << c<<": ";
//        cout << (long long)d/maxTime << endl;
        
        c++;
    }
    
    return 0;
    
}
