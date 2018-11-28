#include <iostream>
#include <vector>

using namespace std;


struct Seat
    {
    int left;
    int right;
    bool used;
    };

int bestBathroom(vector<Seat>bathroom)
    {
    int bestIndex,bestMin=-1,bestMax;
    int cMin,cMax;
    for(int m=1;m<bathroom.size()-1;m++)
        {
        if(bathroom[m].used==false)
            {
            cMin = min(bathroom[m].left,bathroom[m].right);
            cMax = max(bathroom[m].left,bathroom[m].right);
            if(cMin>bestMin)
                {
                bestMin = cMin;
                bestMax = cMax;
                bestIndex = m;
                }
            else if(cMin==bestMin && cMax>bestMax)
                {
                bestMin = cMin;
                bestMax = cMax;
                bestIndex = m;
                }
            }
        }
    return bestIndex;
    }


int main()
    {
    int test;
    cin >> test;
    int n,k;
    int index,iMin,iMax;
    vector<Seat>bathroom;
    for(int i=1;i<=test;i++)
        {
        cin >> n >> k;
        bathroom.resize(n+2);
        bathroom[ 0 ].used = true;
        bathroom[n+1].used = true;
        for(int j=1;j<n+1;j++)
            {
            bathroom[j].used  = false;
            bathroom[j].left  = j-1;
            bathroom[j].right = n-j;
            }
        while(--k)
            {
            index = bestBathroom(bathroom);
            bathroom[index].used  = true;
            bathroom[index].left  = 0;
            bathroom[index].right = 0;
            for(int j=index-1;j>0 && bathroom[j].used==false;j--)
                bathroom[j].right = index-j-1;
            for(int j=index+1;j<n+1 && bathroom[j].used==false;j++)
                bathroom[j].left  = j-index-1;
            }
        index = bestBathroom(bathroom);
        iMin  = min(bathroom[index].left,bathroom[index].right);
        iMax  = max(bathroom[index].left,bathroom[index].right);
        cout << "Case #" << i << ": " << iMax << " " << iMin << endl;
        }
    return 0;
    }
