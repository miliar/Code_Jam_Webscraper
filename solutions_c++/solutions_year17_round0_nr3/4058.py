#include <iostream>
#include <vector>
#include <set>

//TODO: make this solution work for large instances

int f(int n, int k)
{
    if(k == 1)
    {
        return n;
    }
    if(n % 2)
    {
        return f((n-1)/2, k/2);
    }
    else
    {
        if(k % 2)
        {
            return f(n/2 - 1, (k-1)/2);
        }
        else
        {
            return f(n/2, k/2);
        }
    }

}

int main() {
    int num_instances;
    std::cin >> num_instances;
    for (size_t i = 0; i < num_instances; i++)
    {

        int n,k;

        std::cin >> n >> k;

        int res = f(n,k);

        std::cout << "Case #" << i + 1 << ": " << (res-1)/2 + (res-1)%2 << " " << (res-1)/2<< std::endl;
    }
}