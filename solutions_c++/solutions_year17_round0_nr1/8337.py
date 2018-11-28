#include <iostream>
#include <set>
#include <vector>

using namespace std;


int main()
    {
    int test;
    cin >> test;
    int k,len,flips;
    string pancake,objective,temp;
    string happy = "++++++++++";
    set<string>reached;
    vector<string>primary,secondary;
    vector<string>::iterator iVec;
    for(int i=1;i<=test;i++)
        {
        cin >> pancake >> k;
        len = pancake.length();
        objective = happy.substr(0,len);
        reached.clear();
        reached.insert(pancake);
        primary.clear();
        primary.push_back(pancake);
        secondary.clear();
        flips = 0;
        while( primary.size()>0 && reached.find(objective)==reached.end() )
            {
            for(iVec=primary.begin();iVec!=primary.end();iVec++)
                {
                for(int w=0;w+k<=len;w++)
                    {
                    temp = *iVec;
                    for(int j=0;j<k;j++)
                        if(temp[w+j]=='-')
                            temp[w+j] = '+';
                        else
                            temp[w+j] = '-';
                    if(reached.find(temp)==reached.end())
                        {
                        reached.insert(temp);
                        secondary.push_back(temp);
                        }
                    }
                }
            primary.clear();
            primary.swap(secondary);
            flips++;
            }
        cout << "Case #" << i << ": ";
        if( reached.find(objective)==reached.end() )
            cout << "IMPOSSIBLE" << endl;
        else
            cout << flips << endl;
        }
    return 0;
    }
