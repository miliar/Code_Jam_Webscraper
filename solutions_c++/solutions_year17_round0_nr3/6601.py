#include <iostream> 
#include <vector>
#include <deque>
#include <string> 
#include <unordered_map> 
#include <unordered_set>
#include <cmath>

using namespace std;

struct stall
{
    bool occupied;
    int LS;
    int RS;
    
    stall()
    {
        occupied = false;
        LS = -1;
        RS = -1;
    }
};

class bathroom
{
private:
    vector<stall> data;
    int lastLS;
    int lastRS;
    
    int calcLS(unsigned int index)
    {
        for (int i = index; i >= 0; --i)
        {
            if (data[i].occupied)
                return (index - i - 1);
        }
        return index;
    }
    
    int calcRS(unsigned int index)
    {
        for (unsigned int i = index; i < data.size(); ++i)
        {
            if (data[i].occupied)
                return (i - index - 1);
        }
        return (data.size() - index - 1);
    }
    
    int minOf(int a, int b)
    {
        if (a < b)
            return a;
        return b;
    }
    
    int maxOf(int a, int b)
    {
        if (a > b)
            return a;
        return b;
    }
    
    int maxIn(vector<int> &vec)
    {
        int result = vec[0];
        
        for (unsigned int i = 0; i < vec.size(); ++i)
        {
            if (vec[i] > result)
                result = vec[i];
        }
        
        return result;
    }
    
    void setStall(unsigned int index)
    {
        lastLS = data[index].LS;
        lastRS = data[index].RS;
        
        data[index].occupied = true;
        data[index].LS = -1;
        data[index].RS = -1;
    }
    
public:
    bathroom() { }
    
    bathroom(unsigned int N)
    {
        data.resize(N);
        update();
    }
    
    void update()
    {
        for (unsigned int i = 0; i < data.size(); ++i)
        {
            if (!data[i].occupied)
            {
                data[i].LS = calcLS(i);
                data[i].RS = calcRS(i);
            }
        }
    }
    
    void insert()
    {
        vector<int> mins(data.size());
        
        for (unsigned int i = 0; i < data.size(); ++i)
            mins[i] = minOf(data[i].LS, data[i].RS);
        
        
        vector<unsigned int> indexOfMins;
        int maxOfMins = maxIn(mins);
        
        
        for (unsigned int i = 0; i < mins.size(); ++i)
        {
            if (mins[i] == maxOfMins)
                indexOfMins.push_back(i);
        }
        
        
        if (indexOfMins.size() == 1)
            setStall(indexOfMins[0]);
        else
        {
            vector<int> maxs(indexOfMins.size());
            
            for (unsigned int i = 0; i < maxs.size(); ++i)
                maxs[i] = maxOf(data[indexOfMins[i]].LS, data[indexOfMins[i]].RS);
            
            
            int maxOfMaxs = maxIn(maxs);

            vector<unsigned int> indexOfMaxs;
            
            
            for (unsigned int i = 0; i < maxs.size(); ++i)
            {
                if (maxs[i] == maxOfMaxs)
                    indexOfMaxs.push_back(indexOfMins[i]);
            }
            
            setStall(indexOfMaxs[0]);
        }
        
        update();
    }
    
    void solve(unsigned int K)
    {
        for (unsigned int i = 0; i < K; ++i)
            insert();

        cout << maxOf(lastLS, lastRS) << " " << minOf(lastLS, lastRS) << endl;
    }
};

int main()
{
    unsigned short T;
    cin >> T;
    
    for (unsigned int i = 1; i <= T; ++i)
    {
        unsigned int N, K;
        cin >> N >> K;
        bathroom stalls(N);
        cout << "Case #" << i << ": ";
        stalls.solve(K);
    }

}

