#include <iostream>
#include <limits>
#include <vector>

using namespace std;

#define MAXCITIES 100

template<typename T, typename Compare>
class PriorityQueue
{
public:
    PriorityQueue(T* elements, size_t size, Compare comp = Compare())
        : elements(elements), size(size), comp(comp), heap(size), positions(size)
    {
        init();
    }

    void reset()
    {
        size = heap.size();
        init();
    }

    bool empty() const { return size == 0; }

    T& front() { return elements[heap[0]]; }
    const T& front() const { return elements[heap[0]]; }

    void pop()
    {
        --size;
        if (size > 0)
        {
            positions[heap[0]] = std::numeric_limits<size_t>::max();
            size_t idx = heap[size];
            heap[0] = idx;
            positions[idx] = 0;
            down(0);
        }
    }

    void improve(const T* element)
    {
        size_t idx = element - elements;
        up(positions[idx]);
    }

private:
    void init()
    {
        for (size_t i = 0; i < size; ++i)
        {
            heap[i] = i;
            positions[i] = i;
        }
        if (size > 1)
        {
            size_t position = getParent(size - 1);
            while (true)
            {
                down(position);
                if (position == 0)
                    break;
                --position;
            }
        }
    }

    void down(size_t position)
    {
        size_t first = position;
        while (true)
        {
            position = first;
            size_t left = getLeftChild(position);
            size_t right = left + 1;
            if ((left < size) && comp(elements[heap[left]], elements[heap[first]]))
                first = left;
            if ((right < size) && comp(elements[heap[right]], elements[heap[first]]))
                first = right;
            if (first == position)
                break;
            size_t temp = heap[position];
            size_t hf = heap[first];
            heap[position] = hf;
            positions[hf] = position;
            heap[first] = temp;
            positions[temp] = first;
        }
    }

    void up(size_t position)
    {
        while (position != 0)
        {
            size_t parent = getParent(position);
            if (!comp(elements[heap[position]], elements[heap[parent]]))
                break;
            size_t temp = heap[position];
            size_t hp = heap[parent];
            heap[position] = hp;
            positions[hp] = position;
            heap[parent] = temp;
            positions[temp] = parent;
            position = parent;
        }
    }

    static size_t getParent(size_t i) { return (i - 1) / 2; }
    static size_t getLeftChild(size_t i) { return 2 * i + 1; }

private:
    T* elements;
    size_t size;
    Compare comp;
    std::vector<size_t> heap;
    std::vector<size_t> positions;
};

struct Nbh
{
    double cost;
    int city;
};

struct City
{
    vector<Nbh> nbhs;
    double cost;
};

struct CityComp
{
    bool operator()(const City& c1, const City& c2)
    {
        return c1.cost < c2.cost;
    }
};

int n, q;
City cities[MAXCITIES];
int horseDist[MAXCITIES];
double horseSpeed[MAXCITIES];
int cityDists[MAXCITIES];

double solve()
{
    cin >> n >> q;
    for (int i = 0; i < n; ++i)
    {
        cities[i].nbhs.clear();
        cities[i].cost = numeric_limits<double>::max();
        cin >> horseDist[i] >> horseSpeed[i];
    }
    cities[0].cost = 0.0;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            int dist;
            cin >> dist;
            if (j == (i + 1)) {
                cityDists[j] = dist;
            }
        }
    }

    int u, v;
    cin >> u >> v;

    for (int i = 0; i < n; ++i)
    {
        int remDist = horseDist[i];
        int travelled = 0;
        double speed = horseSpeed[i];
        int nextCity = i + 1;
        while ((nextCity < n) && (remDist >= cityDists[nextCity]))
        {
            travelled += cityDists[nextCity];
            remDist -= cityDists[nextCity];
            double cost = (double)travelled / speed;
            cities[i].nbhs.push_back({ cost, nextCity });
            ++nextCity;
        }
    }

    PriorityQueue<City, CityComp> pq(cities, n);
    while (true)
    {
        City& city = pq.front();
        pq.pop();

        size_t idx = &city - cities;
        if (idx == (n-1))
            return city.cost;

        for (const Nbh& nbh : city.nbhs)
        {
            double ncost = city.cost + nbh.cost;
            if (ncost >= cities[nbh.city].cost)
                continue;
            cities[nbh.city].cost = ncost;
            pq.improve(cities + nbh.city);
        }
    }



}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: %.9f\n", i, solve());
    }
}