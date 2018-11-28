#include <string>
#include <iostream>
using namespace std;
int main(int argc, char* argv[])
{
    int T;
    cin >> T;
    for(int t=0; t<T; ++t)
    {
        int K, N;
        cin >> K >> N;
        int bath[1002] = {0};
        bath[0] = 1;
        bath[1001] = 1;
        bath[K+1]=1;
        int resultMax = -1;
        int resultMin = -1;
        for(int p=0; p<N; ++p){
            int tryLeft[10002] = {0};
            tryLeft[0] = -1;
            int leftMax = -1;
            int leftMaxi = -1;
            for(int i=1; i<=K; ++i)
            {
                if(bath[i] == 1)
                {
                    tryLeft[i] = -1;
                    continue;
                }
                if(bath[i] == 0) tryLeft[i] = tryLeft[i-1]+1;                
                if(tryLeft[i]>leftMax)
                {
                    leftMax = tryLeft[i];
                    leftMaxi = i;
                }
            }
            int tryRight[10002] = {0};
            tryRight[K+1] = -1;
            int rightMax = -1;
            int rightMaxi = -1;

            int tryTotal[10002] = {0};
            int tryTotalMax[10002] = {0};
            int totalMax = -1;
            int totalMaxi = -1;

            for(int i=K; i>=1; --i)
            {
                if(bath[i] == 1)
                {
                    tryRight[i] = -1;
                    continue;
                }
                if(bath[i] == 0) tryRight[i] = tryRight[i+1]+1;
                if(tryRight[i]>rightMax)
                {
                    rightMax = tryRight[i];
                    rightMaxi = i;
                }
                if(tryRight[i]<tryLeft[i])
                {
                    tryTotal[i] = tryRight[i];
                    tryTotalMax[i] = tryLeft[i];
                }
                else
                {
                    tryTotal[i] = tryLeft[i];
                    tryTotalMax[i] = tryRight[i];
                }
                if(tryTotal[i]>totalMax || (tryTotal[i]==totalMax && tryTotalMax[i]>=tryTotalMax[totalMaxi]))
                {
                    totalMax = tryTotal[i];
                    totalMaxi = i;
                }
            }
            int lrmax = tryLeft[totalMaxi];
            int lrmin = tryRight[totalMaxi];
            if(lrmax<lrmin) 
            {
                int temp = lrmax;
                lrmax = lrmin;
                lrmin = temp;
            }
            //cout << lrmax << " " << lrmin << endl;
            resultMax = lrmax;
            resultMin = lrmin;
            bath[totalMaxi] = 1;
        }
        cout << "Case #" << (t+1) << ": ";
        cout << resultMax << " " << resultMin << endl;
    }
    return 0;
}