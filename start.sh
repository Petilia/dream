docker-compose -f docker-compose.yml \
               -f assistant_dists/dream_russian_robot/docker-compose.override.yml \
               -f assistant_dists/dream_russian_robot/dev.yml \
               -f assistant_dists/dream_russian_robot/proxy.yml \
               -f assistant_dists/dream_russian_robot/telegram.yml \
               up