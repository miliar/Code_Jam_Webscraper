#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>
#define modulo 666013

using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

struct interval
{
    int x, y;
};

int abs(int x)
{
    if(x < 0)
        x = -x;
    return x;
}


struct compare_cost
{
    bool operator() ( const interval& a, const  interval& b) const
    {
        int mid1, mid2, mid3, mid4;
        mid1 = (a.x + a.y) / 2;
        mid2 = mid1 + 1;
        mid3 = (b.x + b.y) / 2;
        mid4 = mid3 + 1;
        int minim1 = min(abs(a.x- mid1) , abs(a.y- mid2));
        int minim2 = min(abs(b.x- mid3) , abs(b.y- mid4));
        if(minim1 == minim2)
        {
            int maxim1 = max(abs(a.y-mid1), abs(a.x-mid2));
            int maxim2 = max(abs(b.y-mid3), abs(b.x-mid4));

            if(maxim1 == maxim2)
            {
                 return mid1 > mid3;
            }
            return maxim1 < maxim2;
            //fout <<"ajunge aici";


        }
        return minim1 < minim2;

    }
};

priority_queue <interval, vector<interval>, compare_cost > heap;




string sir;
int i, n, k, j,contor,st,dr,x,y,m,t;

int main()
{
    fin >> t;
    for(int r = 1; r <= t; r++)
    {
        fin >> n >> k;
        heap.push({0 , n + 1});
        int maxim , minim;
        for(i = 1; i <= k; i++)
        {
            int x = heap.top().x;
            int y = heap.top().y;
            //fout << x <<" "<<y<<"\n";
            int mid1, mid2;
            mid1 = (x + y) / 2;
            mid2 = mid1 + 1;
            int poz = -1;
            //min(abs(a.x- mid1) , abs(a.y- mid2))
            if(x - mid1 == y - mid2)
            {
               // int maxim1 = max(abs(a.y-mid1), abs(a.x-mid2));
                if(y - mid1 == x - mid2)
                {
                    poz = mid1;
                }
                else
                {
                    if(y - mid1 > x - mid2)
                    {
                        poz = mid1;
                    }
                    else poz = mid2;
                }
            }
            else
            {
                if(x - mid1 < y - mid2)
                {
                    poz = mid1;
                }
                else poz = mid2;
            }
            minim = min(abs(x - poz),abs(y-poz)) - 1;
            maxim = max(abs(x - poz),abs(y-poz)) - 1;

            maxim = max(0, maxim);
            minim = max(0, minim);

            //fout << x <<" "<<y<<"\n";
            //fout <<poz <<"\n";
            //fout <<abs(x-poz)<<abs(y-poz)<<   "\n";
            heap.pop();
            if(x!=poz)
            heap.push({x, poz});
            if(y!=poz)
            heap.push({poz, y});

        }
        while(! heap.empty())
        {
            heap.pop();
        }
        //fout <<"\n\n\n";
        fout << "Case #" << r <<": " << maxim <<" " << minim <<"\n";
    }
    /*heap.push({0,100});
    heap.push({2,80});
    fout<<heap.top().x <<" "<<heap.top().y<<"\n";*/


}
