#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isSorted(int num)
    {        
        vector<int> list;
        while(num > 0)
            {
                list.push_back(num%10);
                num = num/10;
            }
        reverse(list.begin(), list.end());
        int size = list.size();
        for(int i=1; i<size; i++)
            {
                if(list[i] < list[i-1])
                    {
                        return false;
                    }
            }
        return true;
    }
int main()
    {
        int t;
        cin >> t;
        for(int i=1; i<=t; i++)
            {
                int num; 
                cin >> num;
                int num_temp = num;
                while(num_temp > 0)
                    {
                        if(isSorted(num_temp))
                        {
                            cout << "Case #" << i << ": " << num_temp << endl;
                            break;
                        }
                        --num_temp;
                    }
                
            }
    }