#include<iostream>
#include<limits>
#include<fstream>
#include<vector>
#include<inttypes.h>
using namespace std;

struct node {
    node(int dis, int s) : distance(dis), speed(s) {}
    int distance;
    int speed;
};

struct greater_than_key
{
    inline bool operator() (const node& struct1, const node& struct2)
    {
        return (struct1.distance > struct2.distance);
    }
};

double minspeed(std::vector<node> &vec, int total_distance) {

    std::sort(vec.begin(), vec.end(), greater_than_key());
    int length = vec.size();
    double min_time = INT_MIN;
    for (int i =0 ; i < length; i++) {
            float diff_dis = (total_distance - vec[i].distance);
            float hor_speed = vec[i].speed;
            double time = diff_dis/hor_speed;
            //cout << vec[i].distance  << "   " << vec[i].speed << " time: " << time  << endl;
            min_time = std::max(time, min_time);
    }

    return min_time;
}

typedef std::numeric_limits< double > dbl;


int main() {
    int input;
    int total_distance , number_of_horses;
    int horse_distance, horse_speed;
    std::vector<node> horse_vec;
    ifstream file("input.txt");
    file >> input;
    for (int i =0; i< input ; i++) {
        horse_vec.clear();
        file >> total_distance;
        file >> number_of_horses;
        for (int j =0 ; j < number_of_horses ; j++) {
            file >> horse_distance;
            file >> horse_speed;
            node n(horse_distance, horse_speed);
            horse_vec.push_back(n);
        }
        double min_time = minspeed(horse_vec, total_distance);
        double dis = total_distance;
        double min_speed = dis / min_time;
        std::cout << std::fixed;
        cout.precision(6);
        cout << "Case #" << i + 1 << ": "<<  " " << min_speed <<endl;
    }
}
