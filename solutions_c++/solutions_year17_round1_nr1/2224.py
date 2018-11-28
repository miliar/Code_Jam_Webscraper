//
// Created by Snehil Vishwakarma on 4/14/17.
//

#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <numeric>

using namespace std;

int main() {
    int T,r,c;
    cin>>T;
    for(int i=0; i<T; ++i)
    {
        cin>>r>>c;
        vector < vector < char > > arr;
        vector < int > rowpos;
        for(int j=0; j<r; ++j)
        {
            vector < char > temp(c);
            vector < int > pos;
            for(int k=0; k<c; ++k)
            {
                cin >> temp[k];
                if (temp[k] != '?')
                    pos.push_back(k);
            }
            if(pos.size()>0)
            {
                int p=0,k=0;
                while(p<c && k<pos.size())
                {
                    if(p<pos[k])
                        temp[p]=temp[pos[k]];
                    else
                        k++;
                    p++;
                }
                if(p<c)
                {
                    k--;
                    while(p<c)
                    {
                        temp[p]=temp[pos[k]];
                        p++;
                    }
                }
            }
            else
                rowpos.push_back(j);
            arr.push_back(temp);
        }
        int k=0;
        while(k<rowpos.size())
        {
            int up=rowpos[k]-1,down=rowpos[k]+1;
            bool chk=false;
            while(up >= 0 && down < r)
            {
                if(arr[up][0]!='?' || arr[down][0]!='?')
                {
                    chk=true;
                    break;
                }
                up--;
                down++;
            }
            if(!chk)
            {
                while(up >= 0)
                {
                    if(arr[up][0]!='?')
                    {
                        chk=true;
                        break;
                    }
                    up--;
                }
                if(!chk)
                {
                    while(down < r)
                    {
                        if(arr[down][0]!='?')
                        {
                            chk=true;
                            break;
                        }
                        down++;
                    }
                }
            }
            if(up<0)
            {
                for(int z=down-1;z>=rowpos[k];--z)
                    arr[z]=arr[down];
            }
            else
            {
                for(int z=up+1;z<=rowpos[k];++z)
                    arr[z]=arr[up];
            }
            k++;
        }
        cout << "Case #" << (i+1) << ":";
        for(int j=0; j<r; ++j)
        {
            cout << endl;
            for(int k=0; k<c; ++k)
                cout << arr[j][k];
        }
        if(i!=(T-1))
            cout << endl;
    }
    return 0;
}