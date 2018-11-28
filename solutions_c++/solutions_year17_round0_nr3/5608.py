#include <iostream>
using namespace std;

class Range{
public:
    int startP;
    int endP;
    Range(){
        this->startP = 0;
        this->endP = 0;
    }
};

Range findMaxRange(int *arr, int size)
{
    int start = 0;
    int count = 0, maxCount = -1, end = 0;
    Range range;
    while(start < size)
    {
        if(start < size && arr[start] == 1)
        {
            end = start + 1;
            while(end < size && arr[end] != 1)
                end++;
            count = end - start - 1;
            if(count > maxCount)
            {
                maxCount = count;
                range.startP = start + 1;
                range.endP = end - 1;
            }
            start = end;
            continue;
        }
        start++;
    }
    return range;
}

int main()
{
    int T, N, K;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> N >> K;
        int *arr = new int[N+2]{0};
        arr[0] = 1;
        arr[N+1] = 1;
        Range range;
        int mid = 0;
        for(int j = 0; j < K; j++)
        {
            range = findMaxRange(arr, N+2);
            mid = (range.startP + range.endP)/2;
            arr[mid] = 1;
        }
        cout << "Case #" << i+1 << ": " << max(range.endP - mid, mid - range.startP) << " " << min(range.endP - mid, mid - range.startP) << endl;
        delete []arr;
    }
}
