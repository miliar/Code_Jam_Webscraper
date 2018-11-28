#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <sstream>
#include <cstring>
#include <climits>
#include <ctype.h>

using namespace std;

class Seat
{
public:
    Seat()
    {
    }
    Seat(int l,int r,bool occ)
    {
        left = l;
        right = r;
        occuped = occ;
    }
    int left;
    int right;
    bool occuped;
};

int main()
{
 freopen("input.in","r",stdin);
 freopen("output.out","w",stdout);

    int t,n,k;
    cin >> t;

    for(int i = 1 ; i <= t ; i++)
    {
        cin >> n >> k;
        // init seats
        int l = 0 , r = n-1;
        vector <Seat> seats;
        for(int j = 0 ; j < n; j++)
        {
            seats.push_back(Seat(l++,r--,false));
        }
        // get solution
        for(int j = 0 ; j < k; j++)
        {
            vector <int> idxces;
            int mx_min = -1;
            for(int q = 0; q < n; q++)
            {
                if(seats[q].occuped)continue;
                // get max between min left and right
                int temp = min(seats[q].left,seats[q].right);
                if(temp > mx_min)
                {
                    mx_min = temp;
                    idxces.clear();
                    idxces.push_back(q);
                }
                else if(temp == mx_min)
                {
                    idxces.push_back(q);
                }

            }
            // incase of tie , get max between max left nd right
            int mx_mx = -1;
            int res_idx = -1;
            for(int q = 0; q < idxces.size(); q++)
            {
                int temp = max(seats[idxces[q]].left,seats[idxces[q]].right);
                if(temp > mx_mx)
                {
                    mx_mx = temp;
                    res_idx = idxces[q];
                }
            }
            if(j == k-1)
            {
                cout << "Case #"<<i<<": "<<max(seats[res_idx].left,seats[res_idx].right) <<" "<<min(seats[res_idx].left,seats[res_idx].right)<<endl;
            }
            else
            {
                seats[res_idx].occuped = true;
                int v = 0;
                for(int q = res_idx-1;q >= 0 ;q--){
                    if(seats[q].right < v) break;
                    seats[q].right = v++;
                }
                v = 0;
                for(int q = res_idx+1;q < n ;q++){
                    if(seats[q].left < v) break;
                    seats[q].left = v++;
                }
            }
//            cout << seats[n-1].left <<" " << seats[n-1].right <<" "<< seats[n-1].occuped << endl;
        }
    }
    return 0;
}
