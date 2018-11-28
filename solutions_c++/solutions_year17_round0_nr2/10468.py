#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a,b,c;
    vector<int> in,proc;
    bool isTidy;
    cin >> a;
    for(int i=0;i<a;i++)
    {
        int f;
        cin >> f;
        in.push_back(f);
    }
    int no=0;
    for(int b:in)
    {
        no+=1;
        c=b;
        isTidy=false;
        while(!isTidy)
        {
            isTidy=true;
            b = c;
            if(int(b/10)!=0)
            {
                proc.clear();
                while(b!=0)
                {
                    proc.push_back(b % 10);
                    b /= 10;
                }
                for(int i=1;i<proc.size();i++){
                    if(proc[i-1]<proc[i])isTidy=false;
                }
                if(!isTidy) c += - 1;
            }
        }
        isTidy=true;
        cout << "Case #" << no << ": " << c << endl;
    }
    return 0;
}
