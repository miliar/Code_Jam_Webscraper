#define _USE_MATH_DEFINES
#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(int argc, char** argv)
{
    ifstream fin; 
    ofstream fout;
    if (argc != 3)
    {
        cout << "incorrect usage" << endl;
        return -1;
    }
    fin.open(argv[1]);
    if (!fin)
    {
        cout << "input file not open error" << endl;
        return -1;
    }
    fout.open(argv[2]);
    if (!fout)
    {
        cout << "output file not open error" << endl;
        return -1;
    }
    
    int t;
    int n, k;
    fin >> t;
    for (int j = 0; j < t; j++)
    {
        fin >> n >> k;
        int *stall = new(nothrow)int[n + 2];
        for (int i = 0; i < n + 2; i++)
        {
            if (i == 0 || i == n + 1)
                stall[i] = 1;
            else
                stall[i] = 0;
        }
        for (int i = 0; i < k; i++)
        {
            vector<int>maxlr;
            vector<int>minlr;
            vector<int>pos;
            for (int l = 0; l < n + 2; l++)
            {
                int left = 0, right = 0;
                if (stall[l] == 0)
                {
                    pos.push_back(l);
                    int x = l - 1;
                    while (stall[x] == 0)
                    {
                        left++;
                        x--;
                    }
                    x = l + 1;
                    while (stall[x] == 0)
                    {
                        right++;
                        x++;
                    }
                    if (left >= right)
                    {
                        maxlr.push_back(left); //more gap
                        minlr.push_back(right); //less gap            
                    }
                    else
                    {
                        maxlr.push_back(right); //more gap
                        minlr.push_back(left); //less gap                      
                    }
                }
            }
            //finding the max of min(LR)
            int minlrmax = minlr[0];
           vector<int>ind_min;;
            for (int j2 = 0; j2 < minlr.size(); j2++)
            {
                if (minlrmax <= minlr[j2])
                {
                    minlrmax = minlr[j2];
                }
            }
            
            //storing the pos of min & corresponding max
            vector<int> maxd;
            for (int j2 = 0; j2 < minlr.size(); j2++)
            {
                    if (minlrmax == minlr[j2])
                    {
                        ind_min.push_back(pos[j2]);
                        maxd.push_back(maxlr[j2]);
                    }
                 
            }
            vector<int>ind_max;
           int x;
           {
               //if there is only one max of min(lr)
               if (ind_min.size() == 1)
               {
                  stall[ind_min[0]] = 1;
                  x = ind_min[0]; 
               }
               else
               {
                   //checks for max of max(lr) for those min elements
                   int maxlrmax = maxd[0];
                   //finds the max of max(lr) for min elements
                   for (int j1 = 0; j1 < ind_min.size(); j1++)
                   {
                       if (maxlrmax <= maxd[j1])
                       {
                           maxlrmax = maxd[j1];
                       }
                   }
                   //finds all possible max and stores it for the pos
                   for (int j1 = 0; j1 < ind_min.size(); j1++)
                   {
                       if (maxlrmax == maxd[j1])
                       {
                           ind_max.push_back(ind_min[j1]);
                       }
                   }

                   
                   if (ind_max.size() ==1)
                   {
                       stall[ind_max.front()] = 1;
                       x = ind_max.front();
                   }
                   else //if two are present, it choses the leftmost of the max
                   {
                       stall[ind_max.front()] = 1;
                       x = ind_max.front();
                   }
               }
           }
           
           if (i == k - 1)
           {
               int y = x - 1;
               int left1 = 0, right1 = 0;
               while (stall[y] == 0)
               {
                   left1++;
                   y--;
               }
               y = x + 1;
               while (stall[y] == 0)
               {
                   right1++;
                   y++;
               }
               int min = left1;
               int max = right1;
               if (right > left)
               {
                   min = right1;
                   max = left1;
               }
               fout << "Case #" << j + 1 << ": " << max << " " << min << endl;
           }

        }
        delete[] stall;
    }
   
    return 0;
}


