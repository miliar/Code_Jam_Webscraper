#include <iostream>

#include <cstdlib>

using namespace std;
#include <vector>

#include <QFile>
#include <QString>
#include <QTextStream>

#define MIN(x, y) (x <= y) ? x : y;
#define MAX(x, y) (x >= y) ? x : y;

void tidy_numbers(unsigned long long input, FILE *fp)
{
    int i = 0;
    int n, k, size;
    int first_conflict = 0;
    vector<int> number;
    number.clear();

    while(input != 0)
    {
        number.push_back((int)(input % 10));
        input = input / 10;
    }

    size = number.size();

    for(i = size - 1;i > 0;i--)
    {
        n = number.at(i);
        k = number.at(i - 1);

        if(n > k)
        {
            first_conflict = i;
            number.at(i) = n - 1;
            break;
        }
    }


    for(i = first_conflict;i < size;i++)
    {
        if(i == size - 1)
        {
            first_conflict = size - 1;
            break;
        }

        n = number.at(i);
        k = number.at(i + 1);

        if(n < k)
//        {
//            number.at(i) = 9;
            number.at(i + 1) = k - 1;
//        }
        else
        {
            first_conflict = i;
            break;
        }
    }

    for(i = size - 1;i >= 0;i--)
    {
        if(i >= first_conflict)
        {
            if(number.at(i) != 0)
                fprintf(fp, "%d", number.at(i));
        }
        else
            fprintf(fp, "9");
    }

}

bool flip_pancakes(QString str, int start, int len, QString *flipped)
{
    int end = start + len - 1;
    *flipped = str;
    if(end < flipped->size() && end >= 0)
    {
        for(int i = start;i <= end;i++)
        {
            if(flipped->at(i) == '+')
                flipped->replace(i, 1, "-");
            else if(flipped->at(i) == '-')
                flipped->replace(i, 1, "+");
        }

        return true;
    }

    return false;
}

bool pancake_flipper(QString pattern, vector<int> &choices, int len, int *uses)
{
    if(!pattern.contains("-"))
    {
        (*uses) = 0;
        return true;
    }

    QString flipped;
    vector<int> options;

    for(int choice : choices)
        options.push_back(choice);

    for(int choice : choices)
    {
        if(flip_pancakes(pattern, choice, len, &flipped))
        {
            (*uses) += 1;
            auto it = find(options.begin(), options.end(), choice);
            if(it != options.end())
                options.erase(it);

            if(flipped.contains("-"))
            {
                if(!pancake_flipper(flipped, options, len, uses))
                    (*uses) -= 1;
                else
                    return true;
            }
            else
                return true;
        }
    }
    return false;
}


int main(int argc, char *argv[])
{
    int cases, i, uses, len;
    QString input, pattern;
    vector<int> choices;
    QStringList parts;
    QFile file("D:\\GoogleCodeJam\\A-small-attempt0.in");
    FILE *fp = fopen("D:\\GoogleCodeJam\\A-small-output.txt", "a");

    if(fp && file.open(QIODevice::ReadOnly))
    {
        QTextStream stream(&file);
        while(!stream.atEnd())
        {
            cases = stream.readLine().toInt();
            for(i = 1;i <= cases;i++)
            {
                input = stream.readLine();
                parts = input.split(" ", QString::SkipEmptyParts);
                pattern = parts.at(1);
                len = pattern.toInt();
                pattern = parts[0];
                uses = 0;
                for(int i = 0;i < (pattern.size() - len) + 1;i++)
                    choices.push_back(i);

                fprintf(fp, "Case #%d: ", i);
                if(pancake_flipper(pattern, choices, len, &uses))
                    fprintf(fp, "%d\n", uses);
                else
                    fprintf(fp, "IMPOSSIBLE\n");

                choices.clear();
            }
            fclose(fp);
        }
    }
    file.close();
//    QString pattern = "+++++";
//    int len = 4;
//    int uses = 0;
//    vector<int> choices;
//    for(int i = 0;i < (pattern.size() - len) + 1;i++)
//        choices.push_back(i);

//    if(pancake_flipper(pattern, choices, len, &uses))
//        printf("%d\n", uses);
//    else
//        printf("IMPOSSIBLE\n");
    return 0;
}
